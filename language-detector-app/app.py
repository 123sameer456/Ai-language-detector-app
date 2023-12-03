from flask import Flask, request
import requests
import random

app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)





# -------------------------  start audio to text then detect text language   ----------------------------------------------

import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile("urdu.wav") as source:
    audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        print("Text:", text)
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError:
        print("Could not request results; check your network connection")
import openai
# Initialize chat history as an empty list
chat_history = []

# Set up OpenAI API credentials (Uncomment and add your API key)
openai.api_key = 'your api key is here'
user_input =  text
chat_history.append({'role': 'user', 'message': user_input})
completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "you are a language detector. your job is to tell the given is this langauge. suppose , if the user message is in the urdu language then your simply response urdu . it should be general not only for urdu language. sometimes user input in any language and you just tell that the language name "},
                {"role": "user", "content": user_input}
            ],
            max_tokens=10
        )

bot_response = completion['choices'][0]['message']['content']
print("Bot: " , bot_response)
chat_history.append({'role': 'bot', 'message': bot_response})



# -------------------------  end audio to text then detect text language   ----------------------------------------------
