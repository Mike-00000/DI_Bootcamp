from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    description = models.TextField()
    page_count = models.IntegerField()
    categories = models.CharField(max_length=255)
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title

    def get_average_rating(self):
        return self.reviews.aggregate(average_rating=Avg('rating'))['average_rating']

    def get_review_count(self):
        return self.reviews.count()

class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()

def update_book_rating(sender, instance, **kwargs):
    book = instance.book
    reviews = book.bookreview_set.all()
    review_count = reviews.count()
    average_rating = reviews.aggregate(avg_rating=models.Avg('rating'))['avg_rating']
    book.average_rating = average_rating
    book.review_count = review_count
    book.save()

post_save.connect(update_book_rating, sender=BookReview)
