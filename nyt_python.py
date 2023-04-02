import requests
import json

# Fetch the JSON data from the URL
response = requests.get('https://raw.githubusercontent.com/doshea/nyt_crosswords/master/2009/01/01.json')
json_data = json.loads(response.content)

# Print the parsed JSON data
print(json_data)