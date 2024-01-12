# Dwight v0.3.13

***Assistant Regional Manager @ Dunder Mifflin***

***Part-time Windows Voice Assistant.***

Other than being Dunder Mifflin's greatest ever salesman, I can do a lot of things. 
* Try asking me to start a meeting or schedule an event.
* Maybe search the web?
* Tell you the weather or the prayer times.
* Forget about your mouse as I can click buttons on the screen for you.
* Throw away your keyboard, I can write whatever you want!
* Try asking me anything about everything and I may have the answer here or there.

### Prerequisites

- Windows operating system (Dwight is specifically designed for Windows).
  
- Python installed on your system.
  
- Microphone for voice input.

## Step 1: Authentication to G Suite

To be able to access all the awesome G Suite functionalities, you first need to create your own project on the cloud.

1. Head to [Google Cloud Console](https://console.cloud.google.com)
2. From the sidebar under "IAM & Admin" select "Create a Project".
3. After creating the project, from the sidebar under "APIs and Services" click "Enabled APIs & Services".
4. Search for "Google Calendar API" and "Google Sheets API" and enable them both.
5. From the sidebar, select "OAuth consent screen".
6. Pick "External" and press create.
7. Add the app name and your email as the support email. (If you encounter problems in this step add yourself as a collaborator and tester in your project on [Firebase Console](https://console.firebase.google.com).)
8. In the scopes tab, click "ADD OR REMOVE SCOPES" and make sure to check all scopes labeled with "Google Calendar API" or "Google Sheets API".
9. Under "OAuth user cap", add your email as a test user.
10. From the sidebar, click "Credentials".
11. Click "CREATE CREDENTIALS", and then "OAuth client ID".
12. Set the type to "Desktop app", and click create.
13. Download the `.json` file, rename it to `credentials.json`, and put it in the GoogleCalendarManager folder.

*Remember not to share your credentials or tokens with anyone.*

## Step 2: Get your OpenAI API key
1. Head to [OpenAI API Keys](https://platform.openai.com/api-keys) and login to your OpenAI account.
2. Click "Create new secret key".
3. Give it a name and press "Create secret key". 

*This is completely free and there's no need for bank account information*

*Your API key should be kept secret.*

## Step 3: Get started with your assistant!

You're all good to go, just run the `init.exe` file and enjoy!

## To make Dwight run on startup

Create a `.bat` file in the same directory as the `main.py` file and write the following in it:

```bat
@echo off
python path\to\main.py
```

Now press `Win + R` and write `shell:startup`

In the directory that got opened create a `.vbs`` file and write the following in it:

```vbs
CreateObject("Wscript.Shell").Run "path\to\your\.bat file",0,True
```

## Tuning the model's architecture and performance

In the `chatbot/train.py` file, you'll find the following segment:

<img src="https://github.com/ZiadElGafy/Dwight/assets/74333133/2528342a-2e5b-45be-b362-46932b8ea291" width="350" alt="hyperparameters">

Here you can customize how you want the model to learn.

***And that's all! Feel free to customize Dwight and make the experience truly your own.***
