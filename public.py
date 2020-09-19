import requests
import json
from login import login
from headers import set_publish_headers


def get_data():
    data = []
    with open('data.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)
    return data


def publish():
    cookies = login()
    data = get_data()
    for item in data:
        URL = 'https://www.haroldltd.ru/cms2/cat/inscore.php'
        headers = set_publish_headers()
        response = requests.post(
            url=URL, data=item, headers=headers, cookies=cookies)
        print(response.text)
