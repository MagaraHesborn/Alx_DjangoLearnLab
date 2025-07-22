books = Book.objects.filter(name=author_name)
books = Library.objects.get(name=library_name)
librarian = library.librarians