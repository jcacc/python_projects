import os
import requests
import random
import string
import time
from requests.structures import CaseInsensitiveDict
import openai
import json

# Set up the OpenAI API client
# A local environment variable must be setup
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):
    response = openai.Image.create(
        model="image-alpha-001",
        prompt=prompt,
        n=1,
        size="512x512",
        response_format="url"
    )

    image_url = response['data'][0]['url']
    return image_url

def download_image(image_url, output_path):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/octet-stream"

    response = requests.get(image_url, headers=headers)

    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
    else:
        print("Error downloading image:", response.status_code)

def save_response_to_file(prompt, image_url, output_path="responses.txt"):
    with open(output_path, "a") as f:
        f.write(f"Prompt: {prompt}\n")
        f.write(f"Image URL: {image_url}\n")
        f.write(f"Generated Image: {output_path}\n\n")

def generate_unique_filename(extension=".png"):
    timestamp = int(time.time())
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"generated_image_{timestamp}_{random_str}{extension}"

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

if __name__ == "__main__":
    images_directory = "generated_images"
    create_directory_if_not_exists(images_directory)

    prompt = input("Enter a text prompt to generate an image: ")
    image_url = generate_image(prompt)
    unique_filename = generate_unique_filename()
    output_path = os.path.join(images_directory, unique_filename)
    
    download_image(image_url, output_path=output_path)
    save_response_to_file(prompt, image_url, output_path="responses.txt")
    print(f"Image generated and saved as '{unique_filename}' in '{images_directory}' folder")
    print("Responses saved to 'responses.txt'")
