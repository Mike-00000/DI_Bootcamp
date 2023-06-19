import requests
from .models import Book

def populate_books_from_api():
    response = requests.get('https://www.googleapis.com/books/v1/volumes?q=search-terms')
    data = response.json()
    
    for item in data['items']:
        volume_info = item['volumeInfo']
        
        book = Book()
        book.title = volume_info['title']
        book.author = ', '.join(volume_info['authors'])
        book.published_date = volume_info['publishedDate']
        book.description = volume_info['description']
        book.page_count = volume_info['pageCount']
        book.categories = ', '.join(volume_info['categories'])
        book.thumbnail_url = volume_info['imageLinks']['thumbnail']
        book.save()
