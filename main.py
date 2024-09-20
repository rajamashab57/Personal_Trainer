from http import client
import openai
import streamlit as st
import time
import logging
from dotenv import find_dotenv, load_dotenv

# Load environment variables from a .env file
load_dotenv(find_dotenv())

# Set your API key
openai.api_key = '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'

# Define the model
model = "gpt-3.5-turbo-16k"

# Create a conversation (this acts as your assistant)
response = openai.ChatCompletion.create(
    model=model,
    messages=[
        {
            "role": "system",
            "content": """
            You are the best personal trainer and nutritionist who knows how to get clients to build lean muscles.
            You've trained high-caliber athletes and movie stars.
            """
        },
        {
            "role": "user",
            "content": "How do I get started working out to lose weight?"
        }
    ]
)

# Extract the assistant's reply
assistant_reply = response['choices'][0]['message']['content']
print(assistant_reply)

asistant_id = "asst_GIXhUOB0MafQJJ1yO3ge93bM"
thread_id = "thread_q3ltv3tb50au3DMDvaT3TzRL"



import openai
import time
import logging

def wait_for_completion(client, model, messages, sleep_interval=5):
    """
    Waits for the completion of a conversation and prints the elapsed time.
    
    :param client: The OpenAI client object.
    :param model: The model to use (e.g., 'gpt-3.5-turbo').
    :param messages: The list of messages to pass to the model.
    :param sleep_interval: Time in seconds to wait between checks.
    """
    start_time = time.time()
    
    try:
        response = client.ChatCompletion.create(
            model=model,
            messages=messages
        )
        elapsed_time = time.time() - start_time
        formatted_elapsed_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        
        print(f"Run completed in {formatted_elapsed_time}")
        logging.info(f"Run completed in {formatted_elapsed_time}")
        
        # Get the assistant's response
        assistant_response = response.choices[0].message['content']
        print(f"Assistant Response: {assistant_response}")
        
    except Exception as e:
        logging.error(f"An error occurred while retrieving the response: {e}")

# === Example Usage ===
logging.basicConfig(level=logging.INFO)

model = "gpt-3.5-turbo-16k"
messages = [
    {
        "role": "system",
        "content": "You are the best personal trainer and nutritionist who knows how to get clients to build lean muscles."
    },
    {
        "role": "user",
        "content": "How do I get started working out to lose weight?"
    }
]

wait_for_completion(client=openai, model=model, messages=messages)

def get_news(topic):
    url = (
        
        f"https://newsapi.org/v2/everything?q={topic}&apikey=&pagesize=5"
        
        
    )