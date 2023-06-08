from django.urls import path
from . import views

app_name = 'image_share'

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('my-images/', views.my_images, name='my_images'),
]
