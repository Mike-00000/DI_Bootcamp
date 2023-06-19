from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BookReview, Book

@receiver(post_save, sender=BookReview)
def update_book_rating(sender, instance, **kwargs):
    book = instance.book
    average_rating = BookReview.objects.filter(book=book).aggregate(avg_rating=models.Avg('rating'))
    book.rating = average_rating['avg_rating']
    book.save()

