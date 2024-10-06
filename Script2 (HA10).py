from Library import Book, find_most_expensive

book1 = Book("Anna Karenina", "Leo Tolstoy", 1877, 250, stoplist=False)
book2 = Book("Crime and Punishment", "Fyodor Dostoevsky", 1866, 300, stoplist=False)
book3 = Book("The Master & Margarita", "Mikhail Bulgakov", 1967, 290, stoplist=False)

books = [book1, book2, book3]

for book in books:
    book.get_info()

print("The most expensive book is", find_most_expensive(books))

print("I censor Bulgakov's books:")
for book in books:
    book.censor("Mikhail Bulgakov", True)

for book in books:
    book.get_info()
