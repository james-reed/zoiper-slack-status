import requests
import json
import sys

arguments = sys.argv
text = (f'Currently in a call with {arguments[1]}')
url = "https://slack.com/api/users.profile.set"
params = {
        'token': 'YOUR_SLACK_TOKEN_GOES_HERE',
        'profile': json.dumps(
            {
                "status_text": text,
                "status_emoji": ":telephone_receiver:"
            }
        )
}
headers = {'Content-Type': 'application/json'}
r = requests.get(url, params=params, headers=headers)
print(r.url)
print(r.text)
