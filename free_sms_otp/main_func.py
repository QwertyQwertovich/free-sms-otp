import requests
from random import shuffle


def generate_pass(phone, userid, key='textbelt', is_test=False, message='', lifetime=180, length=6, proxy=None,
                  retries=10):
    i = 0
    if proxy is not None:
        shuffle(proxy)
    if is_test:
        test = '_test'
    else:
        test = ''
    params = {'phone': phone, 'userid': userid, 'key': key + test, 'lifetime': lifetime, length: length}
    if message != '':
        params[message] = message
    while i < retries:
        i = i + 1
        try:
            if proxy is not None:
                resp = requests.post('https://textbelt.com/otp/generate', params,
                                     proxies={'https': proxy[i], 'http': proxy[i % len(proxy)]})
            else:
                resp = requests.post('https://textbelt.com/otp/generate', params)
            ans = resp.json()
            if ans['success']:
                return ans
            i = i + 1
        except Exception as e:
            return {'success': False}
            pass
    return {'success': False}


def check_pass(otp, userid, key='textbelt', is_test=False, proxy=None):
    if is_test:
        test = '_test'
    else:
        test = ''
    try:
        if proxy is not None:
            resp = requests.get('https://textbelt.com/otp/verify', {"otp": otp, "userid": userid, "key": key + test},
                                proxies={'https': proxy, 'http': proxy})
        else:
            resp = requests.get('https://textbelt.com/otp/verify', {"otp": otp, "userid": userid, "key": key + test})
        return resp.json()
    except:
        return {"success":False}
