# Knotion
# Ravelry + notion integration
# first part: yarn database

import requests
import json

config_path = "config.json"
with open(config_path, 'r') as configfile:
    config = json.load(configfile)

KNOTION_TOKEN = config['auth']['KNOTION_TOKEN']
DATABASE_ID = config['auth']['DATABASE_ID']
RAVELRY_ID = config['auth']['RAVELRY_ID']
headers = {
    "Authorization": "Bearer " + KNOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}
###########


def readDatabase(DATABASE_ID, headers):
    readURL = f'https://api.notion.com/v1/databases/{DATABASE_ID}'

    res = requests.request("GET", readURL, headers=headers)
    print(res.status_code)


readDatabase(DATABASE_ID, headers)
