from .views import StudentListCreateView, StudentRetrieveUpdateDeleteView, StudentView
from django.urls import path

urlpatterns = [
    path('', StudentView.as_view(), name='student-list'),
    path('<int:pk>/', StudentView.as_view(), name='student-detail'),
]