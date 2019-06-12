# bruteforce the flag by comparing the response cipher
# a cipher will be generated on each connection according to a serect key
# the server provide a encryption service base on this onetime key
# this program is used to compare the generated key and guess the flag

from pwn import *
import string

pool = string.printable
r = remote('crypto.hsctf.com',8111)
r.recvuntil('Here is my super secret message: ')
cipher = r.recvline()[:-1]
print "Cipher :" + cipher
flag = 'hsctf{'
n = 2

while flag[-1]!='}':
  for i in pool:
    payload = flag+i
    r.sendline(payload)
    r.recvuntil('Encrypted: ')
    trial = r.recvline()[:-1]
    check = cipher[:(len(payload)*2)]
    if trial == check:
      flag+=i
      print "flag: {}".format(flag)
      break
