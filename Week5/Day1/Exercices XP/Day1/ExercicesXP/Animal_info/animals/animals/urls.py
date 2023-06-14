from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
# from animals_info.views import load_data, family_detail, animal_detail, animal_list, animal_redirect
from django.contrib import admin
from animals_info import views
from animals_info.views import load_data, family_detail, animal_detail, animal_list, animal_redirect


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('load-data/', load_data, name='load_data'),
    path('family/<int:family_id>/', family_detail, name='family_detail'),
    path('animal/<int:animal_id>/', animal_detail, name='animal_detail'),
    path('animals/', animal_list, name='animal_list'),
    path('animal/<int:animal_id>/redirect/', animal_redirect, name='animal_redirect'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

