import itertools
import os
import string


charset = string.ascii_letters + string.digits
passwordPre = 'k1ll0r'
passwordFile =open('passwords.txt','w')

string =''

for (a,b) in itertools.product(charset,repeat=2):
	string += passwordPre +a +b +'\n'

passwordFile.write(string)
passwordFile.close()