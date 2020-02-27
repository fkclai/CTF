import requests
import hashlib
import re
from bs4 import BeautifulSoup

url="http://docker.hackthebox.eu:30552/"

'''
<html>
<head>
<title>emdee five for life</title>
</head>
<body style="background-color:powderblue;">
<h1 align='center'>MD5 encrypt this string</h1><h3 align='center'>nAKNCbLikwf4Q7XrdtGU</h3><center><form action="" method="post">
<input type="text" name="hash" placeholder="MD5" align='center'></input>
</br>
<input type="submit" value="Submit"></input>
</form></center>
</body>
</html>

'''

r = requests.session()
out=r.get(url)
html=out.text

soup = BeautifulSoup(html, 'html.parser')


h3Tags = soup.find_all('h3')
for tag in h3Tags:
	val = tag.string


hashData=hashlib.md5(val.encode('utf-8')).hexdigest()

replyData ={'hash': hashData}
print(val,hashData)

replyOut = r.post(url=url,data=replyData)
#replyOut = r.post(url=url)

print(BeautifulSoup(replyOut.text, 'html.parser').prettify())
