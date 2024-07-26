#author,isbnno(min 13no),bookname,

# search option(exact match required),bkname,author,isbn
class library:
    def __init__(self,bname,bauthor,isbn):
        self.bname=bname
        self.author=bauthor
        self.isbn=isbn
    def display(self):
        print('bookname is:',self.bname)
        print('bookauthor is:',self.author)
        print('book isbn is:',self.isbn)
class book(library):
    def __init__(self):
        pass
    def sbname(self):
        print(self.bname)
        
book1=library('c','wils',2121212121)
book1.display()

book2=library('python','guido',3131313131)
book2.display()

book3=library('php','john',4141414141)
book3.display()

s=book()
s.sbname()
