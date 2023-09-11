"""
$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}
"""
# step1: convert hex to bin
# step2: reverse the string
# step3: base64 decode

encoded_string = "3d3d516343746d4d6d6c315669563362"
#1:
resault = bytes.fromhex(encoded_string).decode()

#2:
resault = resault[::-1]

#3:
import base64
resault = base64.b64decode(resault).decode()

print('the secret is :', resault)

