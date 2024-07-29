class library:
    def __init__(self):
        self.bname=""
        self.author=""
        self.isbn=""
    def getdata(self):
        self.bname=input('enter the book name:')
        self.author=input('enter the author name:')
        self.isbn=input('enter the book isbn:')
    def display(self):
        print('Name of the book:',self.bname)
        print('Author name is:',self.author)
        print('Book isbn is:',self.isbn)
    def search(self):
        search_term = input("Enter search term: ")
        results = []
        for book in self.books:
            if (search_term.lower() in book.title.lower() or
                search_term.lower() in book.author.lower() or
                search_term.lower() in book.isbn.lower()):
                results.append(book)
        if results:
            print("Search results:")
            for book in results:
                print(f"Title: {library.bname}, Author: {library.author}, ISBN: {library.isbn}")
        else:
            print("No matching books found.")
book=[]
while True:
    print("\n\n********library********\n")
    print("1.Add book\n2.Display books\n3.search items\n4.Exit\n")
    a=int(input('enter the choice:'))
    if(a==1):
        l=library()
        l.getdata()
        book.append(l)
    elif(a==2):
        for i in book:
            l.display()
    elif(a==3):
        search()
    elif(a==4):
        print('exit')
        break
else:
        print('invalid')

