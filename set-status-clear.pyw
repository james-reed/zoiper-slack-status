import requests
import json
import sys

url = "https://slack.com/api/users.profile.set"
params = {
        'token': 'YOUR_SLACK_TOKEN_GOES_HERE',
        'profile': json.dumps(
            {
                "status_text": "",
                "status_emoji": ""
            }
        )
}
headers = {'Content-Type': 'application/json'}
r = requests.get(url, params=params, headers=headers)
print(r.url)
print(r.text)
