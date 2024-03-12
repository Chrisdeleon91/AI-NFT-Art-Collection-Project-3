# Import libraries
from openai import OpenAI
import requests
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

# Set the API key for OpenAI
client = OpenAI(api_key=api_key)

# List of prompts
prompts = [
    "Relive the glory days of gaming with a Classic Arcade Video Game Console, its pixelated graphics and joystick controls evoking memories of dimly lit arcades and high scores.",
    "Step into the shoes of a 90s gamer with a Retro Handheld Video Game Console, its compact design and pixelated screen transporting players back to the era of portable gaming.",
    "Experience the magic of 16-bit gaming with a Vintage Console Video Game Console, its cartridge slot and pixelated sprites offering a nostalgic trip down memory lane.",
    "Rediscover the thrill of multiplayer gaming with a LAN Party Video Game Console, its pixelated controllers and LAN capabilities perfect for gathering friends for epic gaming sessions.",
    "Travel back to the dawn of home gaming with a Pong Console Video Game Console, its simple controls and monochrome graphics a tribute to the game that started it all."
]

# Directory to save the downloaded images
output_directory = "generated_images"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)  

# Call the DALL-E 3 API for each prompt and save the images
for index, prompt in enumerate(prompts):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    # Get the image URL
    image_url = response.data[0].url
    
    # Download the image
    image_data = requests.get(image_url).content
    
    # Create a filename that includes the prompt and the index
    image_filename = f"{prompt[:50].replace(' ', '_').replace('/', '')}_image_{index + 1}.png"
    
    # Save the image to the output directory
    image_path = os.path.join(output_directory, image_filename)
    with open(image_path, 'wb') as image_file:
        image_file.write(image_data)

print("Images downloaded successfully.")