from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Book, BookReview
import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from django.contrib.auth.decorators import login_required


# Create your views here.

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = book.bookreview_set.all()
    average_rating = reviews.aggregate(models.Avg('rating'))
    review_count = reviews.count()
    
    return render(request, 'book_detail.html', {'book': book, 'reviews': reviews, 'average_rating': average_rating, 'review_count': review_count})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def fetch_books_from_api():
    url = "https://www.googleapis.com/books/v1/volumes?q=python"  # Exemple d'URL de requête
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for item in data.get("items", []):
            volume_info = item.get("volumeInfo", {})
            title = volume_info.get("title")
            author = volume_info.get("authors", ["Unknown Author"])[0]
            published_date = volume_info.get("publishedDate")
            description = volume_info.get("description", "")
            page_count = volume_info.get("pageCount", 0)
            categories = ", ".join(volume_info.get("categories", []))
            thumbnail_url = volume_info.get("imageLinks", {}).get("thumbnail")

            # Création de l'instance Book avec les informations récupérées
            book = Book(
                title=title,
                author=author,
                published_date=published_date,
                description=description,
                page_count=page_count,
                categories=categories,
                thumbnail_url=thumbnail_url
            )
            book.save()  # Sauvegarde de l'instance dans la base de données
            return HttpResponse("Books populated successfully.")
    else:
        # Gestion des erreurs de requête
        return HttpResponse("Failed to populate books.")

def populate_books():
    fetch_books_from_api()  # Appelle la fonction pour récupérer les livres de l'API Google Books
    books = Book.objects.all()  # Récupère tous les livres de la base de données
    return render(request, 'populate_books.html', {'books': books})

# Vue pour rechercher des livres
def search_books(request):
    # Code de recherche des livres
    return render(request, 'books/search_books.html', context)

# Vue pour afficher les détails d'un livre
def book_detail(request, book_id):
    # Code pour récupérer les détails du livre
    average_rating = BookReview.objects.filter(book=book).aggregate(Avg('rating'))
    review_count = BookReview.objects.filter(book=book).count()
    context = {
        'book': book,
        'average_rating': average_rating,
        'review_count': review_count
    }
    return render(request, 'books/book_detail.html', context)

# Vue pour écrire une critique de livre
@login_required
def write_review(request, book_id):
    # Code pour enregistrer une critique de livre
    return render(request, 'books/write_review.html', context)

@receiver(post_save, sender=BookReview)
def update_book_rating(sender, instance, **kwargs):
    book = instance.book
    average_rating = BookReview.objects.filter(book=book).aggregate(Avg('rating'))
    book.rating = average_rating['rating__avg']
    book.save()