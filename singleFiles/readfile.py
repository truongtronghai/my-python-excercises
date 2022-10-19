import os
print(os.path.abspath('.'))
# print(os.getcwd())
fin = open('sample.txt')
for l in fin:
    word = l.strip()
    print(word)

def boxPrint(symbol,width,height):
    if len(symbol)!=1:
        raise Exception('Symbol must be one character')
    if width<=2:
        raise Exception('Width must be lager than 2')
    if height<=2:
        raise Exception('Height must be lager than 2')
    
    print(symbol * width)
    for i in range(height-2):
        print(symbol+(' '*(width-2))+symbol)
    print(symbol * width)

for (s,w,h) in {('*',4,4),('0',20,5),('xx',5,5),('z',1,3),('z',3,1)}:
    try:
        boxPrint(s,w,h)
    except Exception as err:
        print('An exception happened:'+str(err))