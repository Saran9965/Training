# working with CSV

#using writer in csv

# import csv
# data=[['name','age','dept'],
#       ['sam',21,'msc'],
#       ['ram',22,'mba'],                           #nested list type
#       ['tom',23,'mca'],
#       ['rack',23,'mcom']]
# with open('data.csv','w',newline='') as file:
#     csvw=csv.writer(file)
#     for row in data:
#         csvw.writerow(row)

#using reader in csv

# import csv
# with open('data.csv','r') as file:
#     csvr=csv.reader(file)
#     for row in csvr:
#         print(row)


# using dictionary to reader a csv 

# import csv
# with open('data.csv','r') as file:
#     csvd=csv.DictReader(file)
#     for row in csvd:
#         print(row['name'])#specific items


# using writer in csv

# import csv
# data=[{'name':'sam','age':20,'city':'chennai'},
#       {'name':'ram','age':21},                              # working with dictionary
#       {'name':'tom','age':22,'city':'vellore'}
# ]
# with open('data.csv','w',newline='')as file:
#     fln=['name','age','city']
#     csvd=csv.DictWriter(file,fieldnames=fln)
#     csvd.writeheader()  
#     csvd.writerows(data)

# import csv
# l=[]
# data=[['name','age','dept'],
#       [input('enter the names:'),
#       input('enter the age:'),
#       input('enter the dept:')],
# ]
# for i in data:
#     l.append(i)
# with open('data.csv','w',newline='')as file:
#     csvw=csv.writer(file)
#     for row in data:
#         csvw.writerow(row)

#python using to sqlite3

# import sqlite3
# con=sqlite3.connect('mca.db')           #create a database connection
# con.execute('''create table if not exists users(
#           id integer primary key,
#           rollno integer,
#           name text not null,
#           age integer)''')
# con.execute(''' insert into users(rollno,name,age)values(?,?,?)''',(101,'sam',21))
# con.execute(''' insert into users(rollno,name,age)values(?,?,?)''',(102,'ram',22))
# con.execute(''' insert into users(rollno,name,age)values(?,?,?)''',(103,'tom',23))
# con.commit()
# result=con.execute('select * from users')
# rows=result.fetchall()      
# for x in rows:
#     print(x)
#con.close()     #close a database

    # update values in a table
# import sqlite3
# con=sqlite3.connect('mca.db') 
# con.execute('''update users set name=? where age=? ''',('rajii',22))
# con.commit()
# result=con.execute('select * from users')
# rows=result.fetchall()      
# for x in rows:
#     print(x)
#con.close()     #close a database

    # delete values in a table
import sqlite3
con=sqlite3.connect('mca.db') 
con.execute('')
con.commit()
result=con.execute('select * from users')
rows=result.fetchall()      
for x in rows:
    print(x)
# con.close()  


