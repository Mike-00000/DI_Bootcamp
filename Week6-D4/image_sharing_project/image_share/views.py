from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .forms import ImageForm, RegisterForm
from .models import Image
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = User.objects.create_user(username=username, password=password, email=email)

            return redirect('index')
    else:
        form = RegisterForm()

    return render(request, 'image_share/registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('image_share/registration/index.html')
    else:
        form = AuthenticationForm()
    return render(request, 'image_share/registration/index.html', {'form': form})

@login_required
def index(request):
    images = Image.objects.all()
    return render(request, 'image_share/index.html', {'images': images})

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('my_images')
    else:
        form = ImageForm()
    return render(request, 'image_share/upload_image.html', {'form': form})


@login_required
def my_images(request):
    images = Image.objects.filter(user=request.user)
    return render(request, 'image_share/my_images.html', {'images': images})


