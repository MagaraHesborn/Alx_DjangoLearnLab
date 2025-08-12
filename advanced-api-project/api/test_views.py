from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITests(APITestCase):
    def setUp(self):
        # Create test user & token
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.token = Token.objects.create(user=self.user)

        # Create an author
        self.author = Author.objects.create(name="John Doe")

        # Create a sample book
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

        # Endpoints
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book.id])
        self.delete_url = reverse('book-delete', args=[self.book.id])

    def authenticate(self):
        """Helper to authenticate a user in test requests."""
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # READ TESTS

    def test_list_books_public(self):
        """Anyone can list books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_book_public(self):
        """Anyone can retrieve a book by ID"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    # CREATE TESTS 

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create books"""
        data = {"title": "New Book", "publication_year": 2021, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """Authenticated users can create books"""
        self.authenticate()
        data = {"title": "New Book", "publication_year": 2021, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Book")

    # UPDATE TESTS
    
    def test_update_book_authenticated(self):
        """Authenticated users can update books"""
        self.authenticate()
        data = {"title": "Updated Book", "publication_year": 2022, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated Book")

    def test_update_book_unauthenticated(self):
        """Unauthenticated users cannot update books"""
        data = {"title": "Updated Book", "publication_year": 2022, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # DELETE TESTS

    def test_delete_book_authenticated(self):
        """Authenticated users can delete books"""
        self.authenticate()
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_delete_book_unauthenticated(self):
        """Unauthenticated users cannot delete books"""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # FILTERING / SEARCH / ORDERING 

    def test_filter_books_by_title(self):
        """Filter books by title"""
        url = f"{self.list_url}?title=Test Book"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
        self.assertTrue(any("Test Book" in b['title'] for b in response.data))

    def test_order_books_by_year(self):
        """Order books by publication_year"""
        Book.objects.create(title="Older Book", publication_year=1990, author=self.author)
        url = f"{self.list_url}?ordering=publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [b['publication_year'] for b in response.data]
        self.assertEqual(years, sorted(years))
