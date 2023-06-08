from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_file = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'image_share'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_count = models.IntegerField(default=0)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
