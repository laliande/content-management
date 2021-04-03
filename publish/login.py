import requests
from publish.headers import set_base_headers, set_login_headers
from config import log

autorization_data = {'login': 'harold', 'password': '@topwatch'}


def get_sid_cookie() -> str:
    ''' Description: sets the primary cookie for the request
        Output: sid cookie

    '''
    headers = set_base_headers()
    URL = 'https://www.haroldltd.ru/cms2'
    response = requests.get(url=URL, headers=headers)
    log.debug('Sid cookie is ' + response.text)
    return response.cookies['sid']


def get_login_cookie() -> dict:
    ''' Description: sets cookies for the login request
        Output: login cookies

    '''
    sid = get_sid_cookie()
    URL = 'https://www.haroldltd.ru/cms2/instruction.php'
    headers = set_login_headers()
    cookies = {'sid': sid}
    response = requests.get(url=URL, headers=headers, cookies=cookies)
    cookies.update({'cms2': response.cookies['cms2']})
    log.debug('cms2 cookie is ' + cookies['cms2'])
    return cookies


def login() -> dict:
    ''' Description: makes a login request and returns cookies after login
        Output: after login cookies

    '''
    headers = set_login_headers()
    cookies = get_login_cookie()
    URL = 'https://www.haroldltd.ru/cms2/login.php'
    response = requests.post(
        url=URL, data=autorization_data, headers=headers, cookies=cookies)
    log.debug('login success')
    return cookies
