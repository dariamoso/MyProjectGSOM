class Book:
    def __init__(self, title, author, year, price, stoplist):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.stoplist = stoplist
        
    def get_info(self):
        print(self.author, self.title, self.year, self.price, self.stoplist)

def find_most_expensive(books):
    most_expensive_book = books[0]
    for book in books:
        if book.price > most_expensive_book.price:
            most_expensive_book = book
    return most_expensive_book

    def set_stoplist(self, value: bool):
        if isinstance(value, bool):
            self.stoplist = value

    def censor(self, author_name, value: bool):
        if self.author == author_name:
            self.stoplist = True