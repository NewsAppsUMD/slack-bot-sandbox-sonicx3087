import os
import json
import requests
from datetime import datetime

from slack import WebClient
from slack.errors import SlackApiError


slack_token = os.environ.get('SLACK_API_TOKEN')
congress_api_key = "cQINbhdhwnBngvCcqxxzq1zbGzATVOTUJoPbOMTW"

client = WebClient(token=slack_token)

url = f"https://api.congress.gov/v3/committee-report/119/hrpt?api_key={congress_api_key}&format=json"

r = requests.get(url)

results = r.json()

first_result = results['reports'][0]

display_url = f"https://www.congress.gov/congressional-report/{first_result['congress']}th-congress/house-report/{first_result['number']}"

display_date = datetime.strptime(first_result['updateDate'], '%Y-%m-%dT%H:%M:%SZ')
formatted_date = display_date.strftime('%B %-d, %Y at %-I:%M%p')
sentence = f"On {formatted_date}, the House published {first_result['citation']}, which is available at {display_url}"

msg = sentence
try:
    response = client.chat_postMessage(
        channel="slack-bots",
        text=msg,
        unfurl_links=True, 
        unfurl_media=True
    )
    print("success!")
except SlackApiError as e:
    assert e.response["ok"] is False
    assert e.response["error"]
    print(f"Got an error: {e.response['error']}")

print(sentence)

#fr_url =  results['reports'][0]['url']

#fr = requests.get(fr_url + f"api_keys{congress_api_key}") #I think some code is missing here

#result = fr.json()

#print(result)

#print(first_result)