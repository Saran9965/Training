# perfect number

for i in range(1,1001):
    c=0
    for j in range(1,i):
        if(i%j==0):
            c=c+j
    if(i==c):
        print(i)


# sum of even number

c=0
for i in range(1,10,1):
    if(i%2==0):
        c=c+i
print(c)


#  prime number

for i in range(1,100):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i,'prime')
      
# while loop
n=1
while n<10:
    print(n)
    n=n+1


# with argument and with return 

def sums(a,b):
    return a+b
print(sums(5,5))


# with argument and without return

def sums(a,b):
    print(a+b)
sums(5,5)


# without argument and with return

def sums():
    a=int(input('no1:'))
    b=int(input('no2:'))
    return a+b
print(sums())

# init

class sam:
    count=0
    def __init__(self):
        print('hi')
        sam.count+=1
sam()
sam()
print(sam.count)


# constructor

class sample:
    count=0
    def __init__(self,name,mark,dept):
        self.name=name
        self.mark=mark
        self.dept=dept
        sample.count+=1
stu1=sample('sam',100,'mba')
print(stu1.name)
print(stu1.mark)
print(stu1.dept)
stu2=sample('ram',150,'mca')
stu2.mark=300
print(stu2.name)
print(stu2.mark)
print(stu2.dept)
stu3=sample('tom',200,'msc')
print(stu3.name)
print(stu3.mark)
print(stu3.dept)
print(sample.count)
