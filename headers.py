def set_base_headers():
    headers = {
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 YaBrowser/20.8.3.112 Yowser/2.5 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'ru,en;q=0.9'
    }
    return headers


def set_login_headers():
    headers = set_base_headers()
    headers.update({
        'Cache-Control': 'max-age=0',
        'Authorization': 'Basic YWRtaW44Nzk6ZGU3N2YwZTU=',
        'Origin': 'https://www.haroldltd.ru',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Sec-Fetch-Site': 'same-origin',
    })
    return headers


def set_publish_headers():
    headers = set_base_headers()
    headers.update({
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": "Basic YWRtaW44Nzk6ZGU3N2YwZTU=",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-fetch-site": "same-origin",
    })
    return headers
