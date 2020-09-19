import requests
import json

URL = 'https://www.haroldltd.ru/cms2/cat/inscore.php'
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Basic YWRtaW44Nzk6ZGU3N2YwZTU=",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1"
}


cookies = dict(sid='vehqg3mroq464lotfpdira6o67',
               session='4d7a9c8171a5bd55604285638c73072d',
               uptocall='1',
               _ym_uid='1600538164119872089',
               _ym_d='1600538164',
               dSesn='a59cdda1-3a1b-638b-993d-67f8fa0e3ff1',
               _userGUID='0:kf9z3j6h:LmYiCWO0ElQQyjIZxqYVGm4mmo8H4TZT',
               _ga='GA1.2.1813463451.1600538164',
               _gid='GA1.2.6792886.1600538164',
               _ym_visorc_7970287='w',
               _dvs='0:kf9z3j6h:tOPs_2i0nntgmTkDoueTbgi74h_aEZRS',
               _ym_isad='2',
               _ym_visorc_24632927='w',
               _ym_visorc_26812653='b',
               dbl='7bde430ae5824971819817f0999b119d',
               fco2r34='7bde430ae5824971819817f0999b119d',
               cms2='s58s87p60adq00bbmfvko6upc4'
               )

data = {
    "vendor": "Tissot",
    "coll": "T-Classic",
    "seoSuffix": '',
    "article": "T109.210.22.031.60",
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

response = requests.post(url=URL, data=data, headers=headers, cookies=cookies)
print(response)
print(response.text)
