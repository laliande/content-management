import requests
import json
from login import login
from headers import set_publish_headers

data = {
    "vendor": "Tissot",
    "coll": "T-Classic",
    "seoSuffix": '',
    "article": "T109.210.22.031.62",
    "sex": "%D3%ED%E8%F1%E5%EA%F1",
    "mechanism": '',
    "diametr": '',
    "thickness": '',
    "corpus": '',
    "glass": '',
    "braslet": '',
    "water": '',
    "function": '',
    "dopoform_fake": '',
    "dopoform": '',
    "form": '',
    "caliber": '',
    "colorDial": '',
    "colorWristlet": '',
    "exit": '',
    "price": '',
    "youtube": '',
    "id": '',
    "update": ''
}


def publish(data):
    URL = 'https://www.haroldltd.ru/cms2/cat/inscore.php'
    headers = set_publish_headers()
    cookies = login()
    response = requests.post(
        url=URL, data=data, headers=headers, cookies=cookies)
    print(response.text)


publish(data)
