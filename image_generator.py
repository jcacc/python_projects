import os
import requests
import random
import string
import time
from requests.structures import CaseInsensitiveDict
import openai
import json

# Set up the OpenAI API client
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):
    # Call the DALL-E API to generate an image based on the prompt
    response = openai.Image.create(
        model="image-alpha-001",
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="url"
    )

    image_url = response['data'][0]['url']
    return image_url

def download_image(image_url, output_path="output.png"):
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
        f.write(f"Image: {unique_filename}\n")
        f.write(f"Image URL: {image_url}\n\n")

def generate_unique_filename(extension=".png"):
    timestamp = int(time.time())
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return f"generated_image_{timestamp}_{random_str}{extension}"

if __name__ == "__main__":
    prompt = input("Enter a text prompt to generate an image: ")
    image_url = generate_image(prompt)
    unique_filename = generate_unique_filename()
    download_image(image_url, output_path=unique_filename)
    save_response_to_file(prompt, image_url, output_path="responses.txt")
    print(f"Image generated and saved as '{unique_filename}'")
    print("Responses saved to 'responses.txt'")
