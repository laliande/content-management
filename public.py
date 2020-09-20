import urllib.parse
import ast
import binascii
import requests
import json
from login import login
from headers import set_publish_headers


def get_data():
    data = []
    with open('data.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    return data


def encode(data):
    result = ''
    for key, value in data.items():
        value = urllib.parse.quote(value.encode('cp1251'))

        result = result + key + '=' + value + '&'
    return result[0:-1]


def publish():
    cookies = login()
    data = get_data()
    for item in data:
        item = encode(item)
        URL = 'https://www.haroldltd.ru/cms2/cat/inscore.php'
        headers = set_publish_headers()
        response = requests.post(
            url=URL, data=item, headers=headers, cookies=cookies)
        print(response.text)