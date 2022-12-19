#Knotion
# Ravelry + notion integration
# first part: yarn database

import requests, json

config_path = "config.json"
with open(config_path,'r') as configfile:
    config = json.load(configfile)

KNOTION_TOKEN = config['auth']['KNOTION_TOKEN']
print(KNOTION_TOKEN)
# DATABASE_ID = 

# RAVELRY_ID = ''
