import requests
import json
from collections import OrderedDict
from yaml import dump
from json import dump as toJson
from pathlib import Path

GITMOJIS_URL = "https://raw.githubusercontent.com/carloscuesta/gitmoji/master/src/data/gitmojis.json"
PACKAGE_VERSION = "2.0.0"
PACKAGE_FILE = Path(f'./gitmojis/{PACKAGE_VERSION}/package.yml')
print(Path('.').absolute())

def fetch_gitmojis():
    r = requests.get(GITMOJIS_URL)
    return r.json()

def transformToKeyValue(gitmojis_dict):
    gitmojis = gitmojis_dict['gitmojis']
    return { gitmoji['code']: gitmoji['emoji'] for gitmoji in gitmojis }

gitmojis = transformToKeyValue(fetch_gitmojis())

output = {
    "name": "gitmojis",
    "parent": "default",
    "matches": [ {'trigger': gitmoji, 'replace': emoji} for (gitmoji, emoji) in gitmojis.items() ]
}

yml = dump(output, indent=2,  default_flow_style=False)
with open(PACKAGE_FILE, 'w') as f:
    f.write(yml)
