import re
givenInput=input()
givenInput=givenInput.replace(' ', '')
operand = re.findall('\w', givenInput)
num = re.findall('[0-9]+', givenInput)
parameter=re.findall('x',givenInput)
if len(parameter)==2:
    if givenInput[0]=='-':
        if givenInput[1]=='x':
            a=-1
            if givenInput[3]=='x':
                b=1
                c=int(num[0])
            else:
                b=int(num[0])
                c=int(num[1])

        else:
            a=0-int(num[0])
            if givenInput[3]=='x':
                b=1
                c=int(num[1])
            else:
                b=int(num[1])
                c=int(num[2])
    else:
        if givenInput[1] == 'x':
            a = 1
            if givenInput[3] == 'x':
                b = 1
                c = int(num[0])
            else:
                b = int(num[0])
                c = int(num[1])

        else:
            a = 0 - int(num[0])
            if givenInput[3] == 'x':
                b = 1
                c = int(num[1])
            else:
                b = int(num[1])
                c = int(num[2])
