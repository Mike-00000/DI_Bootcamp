"""
URL configuration for animals project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from animals_info.views import load_data, family_detail, animal_detail


urlpatterns = [
    path('load-data/', load_data, name='load_data'),
    path('family/<int:family_id>/', family_detail, name='family_detail'),
    path('animal/<int:animal_id>/', animal_detail, name='animal_detail'),
]
