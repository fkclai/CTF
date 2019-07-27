import itertools


stuff='01'
directoryPre = ''
directoryFile =open('directorys.txt','w')

string =''
print('start..')

for (a,b,c,d,e,f,g,h,i,j) in itertools.product(stuff,repeat=10):
    string += directoryPre + a+b+c+d+e+f+g+h+i+j +'\n'

directoryFile.write(string)
directoryFile.close()
