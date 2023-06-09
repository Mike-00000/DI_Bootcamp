from django.urls import path
from . import views
from .views import HomeView

app_name = 'visitors'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('hotel-info/', views.hotel_info, name='hotel-info'),
    path('room-availability/', views.room_availability, name='room-availability'),
    # Autres URLs pour les fonctionnalités de l'interface des visiteurs
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
