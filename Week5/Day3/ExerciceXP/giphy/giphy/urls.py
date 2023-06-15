from django.contrib import admin
from django.urls import path
from gifs import views
from django.conf import settings
from django.conf.urls.static import static
from gifs.views import increment_like, decrement_like

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('new_gif/', views.new_gif, name='new_gif'),
    path('new_category/', views.new_category, name='new_category'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('categories/', views.categories, name='categories'),
    path('gif/<int:gif_id>/', views.gif, name='gif'),
    path('populate-gifs/', views.populate_gifs_view, name='populate-gifs'),
    path('increment-like/<int:gif_id>/', views.increment_like, name='increment-like'),
    path('decrement-like/<int:gif_id>/', views.decrement_like, name='decrement-like'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
