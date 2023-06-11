from django.contrib import admin
from django.urls import path, include
from student.views import StudentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentView.as_view(), name='student-detail'),
]
