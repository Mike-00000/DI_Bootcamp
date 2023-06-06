from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from accounts.forms import SignupForm, LoginForm

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Enregistrez les données du formulaire et créez un nouvel utilisateur
        form.save()

        # Récupérez le nom d'utilisateur et le mot de passe saisis
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        # Authentifiez l'utilisateur
        user = authenticate(username=username, password=password)

        # Vérifiez si l'utilisateur existe et connectez-le
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'Inscription réussie. Vous êtes maintenant connecté.')

        return super().form_valid(form)

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class ProfileView(DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user'

class LoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/films/homepage/')  # Redirige vers la page d'accueil des films
        else:
            return redirect('/accounts/login/')  # Redirige vers la page de connexion en cas d'échec de l'authentification

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/films/homepage/')  # Redirige vers la page d'accueil des films après la déconnexion

def profile_view(request, user_id):
    # Fetch the user based on the provided ID
    user = get_object_or_404(User, id=user_id)

    # Render the profile template and pass the user object as context
    return render(request, 'accounts/profile.html', {'user': user})

def logout_view(request):
    logout(request)
    return redirect('homepage')
