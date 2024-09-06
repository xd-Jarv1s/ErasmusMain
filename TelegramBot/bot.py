import json
import re
import requests

# Load the JSON file
with open('dataClean.json', 'r') as file:
    data = json.load(file)

# Access the specific data
specific_data = data[0]["data"][15]
# print(specific_data)

# Define regex patterns
date_pattern = r'"Datum":"(\d{2}\.\d{2}\.\d{4})"'
slug_pattern = r'"slug":"([^"]+)"'
id_pattern = r'"_id":"([^"]+)"'
pattern_title = r'"title":"([a-zA-Z\s]+)"'

# Extract data based on patterns
dates = re.findall(date_pattern, specific_data)
slugs = re.findall(slug_pattern, specific_data)
ids = re.findall(id_pattern, specific_data)
titles = re.findall(pattern_title, specific_data)

# Ensure all lists have the same length
min_length = min(len(dates), len(slugs), len(ids), len(titles))

# Initialize index
index = 0

# Use a while loop to process each set of values
while index < min_length:
    date = dates[index]
    slug = slugs[index]
    id_ = ids[index]
    title = titles[index]

    # Construct the output URL
    link = f"https://frey-tag.at/kalender/{slug}?s={id_}"

    # Print the combined results and the link
    print(f"Title: {title}")
    print(f"Date: {date}")
    print(f"Link: {link}")
    print("-----------")

    # Increment the index
    index += 1

    # Your Telegram bot token
    token = '7162097876:AAE27cvUGt6tUzuX3NI9VoNnoUsbNYYnBUM'
    method = "sendMessage"

    # Make a POST request to the Telegram API
    response = requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(token, method),
        data={'chat_id': -1002230118853, 'text': 'hello friend'}
    ).json()
