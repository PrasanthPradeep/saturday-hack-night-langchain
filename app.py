import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
from langchain.llms import HuggingFacePipeline

def get_youtube_video_id(url):
    from urllib.parse import urlparse, parse_qs
    query = urlparse(url)
    if query.hostname == 'youtu.be': 
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    return None

def get_transcript(video_id):
    return YouTubeTranscriptApi.get_transcript(video_id)

def chunk_text(text, chunk_size=500):
    """Splits the text into chunks of the specified size."""
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield ' '.join(words[i:i + chunk_size])

def summarize_transcript(transcript):
    text = " ".join([entry['text'] for entry in transcript])
    summarizer = pipeline("summarization")
    summarized_chunks = [summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
                         for chunk in chunk_text(text)]
    summarized_text = " ".join(summarized_chunks)
    return summarized_text

def main():
    st.title("YouTube Video Summarizer")
    st.write("Enter the URL of a YouTube video to get a summary of its transcript.")
    
    url = st.text_input("YouTube URL", "")
    if url:
        video_id = get_youtube_video_id(url)
        if video_id:
            with st.spinner('Fetching transcript...'):
                transcript = get_transcript(video_id)
            with st.spinner('Summarizing transcript...'):
                summary = summarize_transcript(transcript)
            st.subheader("Summary")
            st.write(summary)
        else:
            st.error("Invalid YouTube URL")

if __name__ == "__main__":
    main()
