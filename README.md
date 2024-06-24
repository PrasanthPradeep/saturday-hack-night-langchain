

![LangChain notion](https://github.com/TH-Activities/saturday-hack-night-template/assets/117498997/af58a18d-932c-4ee7-870b-20820cfa3f3f)




# ChatBuddy 🤖💬

Hi there! I'm Chatbuddy , your AI companion powered by the Llama 2 model🦙. Let's chat - I'm ready for fun, informative, and natural conversations on anything you like! 

## Team members
1. [Nobin Sijo](https://www.linkedin.com/in/nobin-sijo-a22711291)
2. [Prasanth P](https://www.linkedin.com/in/prasanth1010000)

## Link to product walkthrough

#



https://github.com/PrasanthPradeep/saturday-hack-night-langchain/assets/78849206/79a193e4-751b-4683-82cc-634fb901aeff



#
#

## How it Works ?
1. Paste Replicate API
2. Press Enter.
3. Enter your prompt
4. Get amazed by the conversation
   
## Libraries used
Python 3<br>
LangChain<br>
Llama2-13B<br>
Llama2-7B<br>
Streamlit<br>
Replicate API<br>

## How to configure
Instructions for setting up project

### Running it locally

Install the required packages:

```bash
pip install -r requirements. txt
```
### Setting Virtual Environment
For Linux
```bash
python3 -m venv venv
```
For Windows
```bash
py -m venv venv
```
### Activate Virtual Environment
```bash
 source venv/bin/activate
```

### Getting your own Replicate API token

To use this app, you'll need to get your own [Replicate](https://replicate.com/) API token.

After signing up to Replicate, you can access your API token from [this page](https://replicate.com/account/api-tokens).
![image](https://github.com/PrasanthPradeep/saturday-hack-night-langchain/assets/143606368/30b17fa5-384e-48a2-ac8b-30cfd0500dca)

### Authenticate Replicate API
1. Open Terminal
2. Locate the directory of Chatbuddy usind "cd" command
3. Enter into Nano Editor
   

  
   

```bash
nano .streamlit/secrets.toml
```
4. Enter this format
   
```bash
[Your API Key]
# Example: for database connection
db_username = "your_github_username"
db_password = "your_github_password"
```
5. Save Nano File by Ctrl+X and Press Y and Enter
6. Run the "run streamlit_app.py" and get amazed

### If any problem persists
1. Open streamlit_app_v2.py file
2. On line 5 "os.environ['REPLICATE_API_TOKEN'] = 'Replace with your API Key' "


## How to Run
Instructions for running

Run the streamlit app:

```bash
streamlit run streamlit_app.py
```
You can also try out the models:
- [Llama2-13B](https://replicate.com/a16z-infra/llama13b-v2-chat)
- [Llama2-70B](https://replicate.com/replicate/llama70b-v2-chat)

[Also find our Youtube Summarizer app we made here](https://github.com/PrasanthPradeep/saturday-hack-night-langchain/tree/master)



