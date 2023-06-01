from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"



class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_completion = models.DateTimeField(null=True, blank=True)
    deadline_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"



work = Category(name="Work")
home = Category(name="Home")
shopping = Category(name="Shopping")
studies = Category(name="Studies")
social = Category(name="Social")

