import requests
from dotenv import load_dotenv
import os

load_dotenv()
canvas_token = os.getenv('CANVAS_TOKEN')

url = 'https://q.utoronto.ca/api/v1/courses'

# Set up the headers
headers = {
    'Authorization': f'Bearer {canvas_token}'
}

# Make the GET request
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    course_objects = response.json()
    for obj in course_objects:
        print(obj['name'])
else:
    print(f'Failed to fetch data: {response.status_code}')

