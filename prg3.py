
# error handling

try:
    a=int(input('enter:'))
    b=int(input('enter:'))
    print(a+b)
except:
    print('invalid')

try:
    a=int(input('data1:'))
    b=int(input('data2:'))
    print(a+c)
except ValueError:
    print('invalid data')
except NameError:
    print('invalid variable')
finally:
    print('sucess')

def cal():
        try:
            beg=int(input('start'))
        except:
            print('type a valid number')
        try:
            fin=int(input('units:'))
        except:
            print('type a valid number')
        try:
            time=int(input('times:'))
        except:
            print('type a valid number')
        try:
            c=(((fin/beg)**(1/time))-1) # type: ignore
            return c
        except ZeroDivisionError:
            print('cannot divisible by 0')
while True:
    data=cal()
    if data:
        print(data)
        break
        

def cal():
 while True:
    beg=input('begin no:')
    if(beg.isdigit() and beg!=0):
        beg=int(beg)
        break
    else:
        print('invalid begin number')
 while True:
    fin=input('final no:')
    if(fin.isdigit()):
        fin=int(fin)
        break
    else:
        print('invalid begin number')
 while True:
    time=input('time no:')
    if(time.isdigit() and time!=0):
        time=int(time)
        break
    else:
        print('invalid begin number')
 c=(((fin/beg)**(1/time))-1)
 return c

data=cal()
print(data)

# file handling

import os
print('1.see all files\n2.write a file \n3.read a file\n4.append')
while True:
    x=int(input('enter the choice:'))
    if(x==1):
        data=os.listdir()
        print(data)
    elif(x==2):
        data=os.listdir()
        print(data)
        x=input('file name:')
        f=open(x,'w')
        s=input('write a content:')
        f.write(s)
        f.close()
    elif(x==3):
        data=os.listdir()
        print(data)
        l=[]
        for i in data:
            if i.endswith('txt'):
                l.append(i)
        print(l)
        a=input('file name:')
        for i in data:
            if(i==a and a.endswith('.txt')):
                f=open(a,'r')
                print(f.read())
                f.close()
                break
        else:
            print('no such files')
    elif(x==4):
        data=os.listdir()
        print(data)
        l=[]
        for i in data:
            if i.endswith('txt'):
                l.append(i)
        print(l)
        c=input('file create:')
        f=open(c,'a')
        b=input('appending a file:')
        f.write(b)
        f.close()
        f=open(c,'r')
        print(f.read())
        break
