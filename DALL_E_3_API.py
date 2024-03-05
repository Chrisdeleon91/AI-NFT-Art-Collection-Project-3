# Import libraries
# import openai
from openai import OpenAI

import webbrowser
import os

# Function to read API key from text file
def read_api_key(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('SECRET KEY'):
                api_key = line.split('=')[1].strip().strip('"')
                return api_key
    return None

# Path to the text file containing the API key
API_KEY_FILE = "OPENAI_API_KEY.txt"

# Read API key from file
api_key = read_api_key(API_KEY_FILE)

client = OpenAI(api_key=api_key)
# Set the API key for OpenAI

# # Call the DALL-E 3 API
response = client.images.generate(
 model="dall-e-3",
 prompt="The Fairchild Channel F Game Console in 8-bit style with a solid background",
 size="1024x1024",
 quality="standard",
 n=1,
)

# Open the generated image in the default web browser
webbrowser.open(response.data[0].url)
