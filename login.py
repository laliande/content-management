import requests
from headers import set_base_headers, set_login_headers
autorization_data = {'login': 'harold', 'password': '@topwatch'}


def get_sid_cookie():
    headers = set_base_headers()
    URL = 'https://www.haroldltd.ru/cms2'
    response = requests.get(url=URL, headers=headers)
    return response.cookies['sid']


def get_login_cookie():
    sid = get_sid_cookie()
    URL = 'https://www.haroldltd.ru/cms2/instruction.php'
    headers = set_login_headers()
    cookies = {'sid': sid}
    response = requests.get(url=URL, headers=headers, cookies=cookies)
    cookies.update({'cms2': response.cookies['cms2']})
    return cookies


def login():
    headers = set_login_headers()
    cookies = get_login_cookie()
    URL = 'https://www.haroldltd.ru/cms2/login.php'
    response = requests.post(
        url=URL, data=autorization_data, headers=headers, cookies=cookies)
    return cookies
