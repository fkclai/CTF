import string

message= 'hihijrijrijr-balrgralrijr-htjrzhujrz-bfnf'

alph_string = string.ascii_lowercase # string of lowercase letters

def CaesarCipherDecoder(message,shift):
    result=''
    for char in message:
        if char in alph_string:
            result = result + charShift(char,shift)
        else:
            result = result + char
    return result        

def charShift(char,shift):
    return ''.join([chr(ord(char)+shift) if chr(ord(char)+shift) in alph_string else chr(ord(char)+shift-len(alph_string))])


for key in range(len(alph_string)):
    print('result #%s: %s' % (key,CaesarCipherDecoder(message,key)))
