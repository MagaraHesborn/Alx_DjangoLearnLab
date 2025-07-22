from relationship_app.models import Library, Book, Author, Librarian

library_name = "Main Library"
author_name = "Hesborn Magara"

library = Library.objects.get(name=library_name)
author = Author.objects.get(name=author_name)

books = library.books.all()
librarian = library.librarians
books_by_author = Book.objects.filter(author=author)
