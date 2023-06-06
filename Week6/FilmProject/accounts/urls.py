from django.urls import include, path
from . import views
from accounts.views import SignupView, LoginView, LogoutView, ProfileView, CustomLoginView, logout_view

urlpatterns = [
    # Other routes
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:user_id>/', ProfileView, name='profile'),
    path('accounts/', include('accounts.urls')),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
   

]