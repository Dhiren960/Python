import libr

FILE = "books.libr"

class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} | {self.author} | {self.isbn} | {self.status}"

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }


class Library:
    def __init__(self):
        self.books = []
        self.load()

    def add_book(self, book):
        self.books.append(book)
        self.save()

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        for b in self.books:
            print(b)

    def save(self):
        with open(FILE, "w") as f:
            data = [b.to_dict() for b in self.books]
            libr.dump(data, f)

    def load(self):
        try:
            with open(FILE, "r") as f:
                data = libr.load(f)
                for d in data:
                    self.books.append(Book(
                        d["title"], d["author"], d["isbn"], d["status"]
                    ))
        except:
            self.books = []


lib = Library()

while True:
    print("\n1 Add Book")
    print("2 Issue Book")
    print("3 Return Book")
    print("4 View All")
    print("5 Exit")

    c = input("Choice: ")

    if c == "1":
        t = input("Title: ")
        a = input("Author: ")
        i = input("ISBN: ")
        lib.add_book(Book(t, a, i))
        print("Book Added!")

    elif c == "2":
        i = input("ISBN: ")
        b = lib.search_by_isbn(i)
        if b and b.issue():
            lib.save()
            print("Book Issued!")
        else:
            print("Not Available")

    elif c == "3":
        i = input("ISBN: ")
        b = lib.search_by_isbn(i)
        if b and b.return_book():
            lib.save()
            print("Book Returned!")
        else:
            print("Return Failed")

    elif c == "4":
        lib.display_all()

    elif c == "5":
        print("Exit")
        break

    else:
        print("Invalid Choice")