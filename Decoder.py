import base64

#crypText="9P&;gFD,5.BOPCdBl7Q+@V'1dDK?qL"
crypText="ubj ner lbh sevraq"

def base64decode(cryptoText):
  for method in dir(base64):
    try:
      if 'decode' in method:
        func = getattr(base64, method)
        print("base64:",method,":", func(cryptoText))
    except:
      pass

def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

result =""
for num in range(-2,2):
  print(rot_alpha(0)(result))
  for word in crypText:
    result +=(chr(ord(word)+num))
  try:
    for rotNum in range(10,50):
      print("ROT",rotNum,":",rot_alpha(rotNum)(result))
  except:
    pass
  try:
    base64decode(result)
  except:
    pass

  result=""
