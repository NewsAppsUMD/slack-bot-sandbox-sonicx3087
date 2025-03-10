import os
import json
import requests

congress_api_key = "cQINbhdhwnBngvCcqxxzq1zbGzATVOTUJoPbOMTW"

url = f"https://api.congress.gov/v3/committee-report/119/hrpt?api_key={congress_api_key}&format=json"

print(url)

r = requests.get(url)

results = r.json()

print(results['reports'][0]['url'])