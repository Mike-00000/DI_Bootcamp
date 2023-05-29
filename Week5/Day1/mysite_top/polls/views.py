from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

def posts(request):

    # some_text = "This is my first page"
    today = date.today()
    title = 'MY FIRST SITE'
    content = 'bla bla bla bla bla'
    author = 'John Doe'
    subscribers = ['Yossi', 'Michael', 'Evgenii', 'Ilona']
    profile = {}

    context = {'time': today,
               'title' : title,
               'content' : content,
               'author' : author,
               'subscribers_list' : subscribers,
               'profile_user' : profile}
    
    return render(request, 'posts.html', context)

def profile(request):

    context = {
        'name' : 'Yossi',
        'hobbies' : ['sleep', 'drink water', 'eat'],
        'gender' : 'M'
    }

    return render(request, 'profile_user.html', context)