# list operations
l=[1,2,'sam',4.0,8]
l.append(7)
l.insert(5,77)
l +=[99]
l.extend([91,98,97])
print(l)

del l[3]
l.pop()
print(l)

for i in l:
    print(i)

li=[[1,2,3],[4,5,6],['sam','ram']]
for i in li:
    for j in i:
        print(j)

li=[2,4.0,20,7,4.4,10]
li2 =[]
for i in li:
    if(i%2==0 and type(i)==float):
        li2.append(i)
    else:
        print(i)


# dictionary

d={'name':'samraj','age':20,'dept':'msc'}
print(d.keys())
print(d.values())
print(d.items())
d['place']='utr'
d.update({'age':22,'dict':'kpm'})
print(d)
