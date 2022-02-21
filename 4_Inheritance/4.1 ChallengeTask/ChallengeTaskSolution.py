class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, publisher, price, period):
        Publication.__init__(self, title, price)
        self.period = period
        self.publisher = publisher


class Book(Publication):
    def __init__(self, title, author, pages, price):
        Publication.__init__(self, title, price)
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        Periodical.__init__(self, title, publisher, price, period)


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        Periodical.__init__(self, title, publisher, price, period)


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

# print(b1.author)
# print(n1.publisher)
# print(b1.price, m1.price, n1.price)

print(isinstance(b1, Book)) # True
print(isinstance(b1, Newspaper)) # False
print(isinstance(b1, Publication)) # T/F?

print(isinstance(m1, Magazine)) # True
print(isinstance(m1, Periodical)) # True
print(isinstance(m1, Publication)) # True

p1 = Periodical("Scientific American", "Springer Nature", 5.99, "Monthly")
print(isinstance(p1, Magazine), "isinstance(p1, Magazine)") # T/F? F
print(isinstance(p1, Publication), "isinstance(p1, Publication)") # T/F? T
print(isinstance(p1, Periodical), "isinstance(p1, Periodical)") # T/F? T