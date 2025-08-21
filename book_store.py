
class Book:
    def _init_(self,title,author,isbn,publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
            current_year = 2025
            return current_year - self.publication_year

    def get_summary(self):
            return ("title, author, publication_year")

book1 = Book("1984", "traveller", "123456", 1950)

print(book1.get_summary())