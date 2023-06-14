from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from info import views

urlpatterns = [
    path('family/<int:family_id>/', views.family_detail, name='family_detail'),
    path('animal/<int:animal_id>/', views.animal_detail, name='animal_detail'),
    path('animals/', views.animal_list, name='animal_list'),
    path('admin/', admin.site.urls),
    path('song/', views.children_song, name='children_song'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)