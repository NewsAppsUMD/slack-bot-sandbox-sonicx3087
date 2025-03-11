import os
import json
import requests

congress_api_key = "cQINbhdhwnBngvCcqxxzq1zbGzATVOTUJoPbOMTW"

url = f"https://api.congress.gov/v3/committee-report/119/hrpt?api_key={congress_api_key}&format=json"

print(url)

r = requests.get(url)

results = r.json()

fr_url =  results['reports'][0]['url']

fr = requests.get(fr_url + f"api_keys{congress_api_key}") #I think some code is missing here

result = fr.json()

print(result)