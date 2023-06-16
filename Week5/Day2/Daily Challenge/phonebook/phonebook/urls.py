
from django.contrib import admin
from django.urls import path
from phonebookapp.views import search_by_phonenumber, search_by_name, search_person


urlpatterns = [
    path('admin/', admin.site.urls),
    path('persons/phonenumber/<str:phonenumber>/', search_by_phonenumber, name='search_by_phonenumber'),
    path('persons/name/<str:name>/', search_by_name, name='search_by_name'),
    path('persons/search/', search_person, name='search_person'),
]
