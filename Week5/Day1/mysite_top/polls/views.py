from django.shortcuts import render
from .models import Post, Person, Email, Category
from .forms import CategoryForm, PostForm, SearchForm

current_user = Person.objects.get(first_name = 'Yossi')


def add_post_view(request):

    if request.method == 'POST':
        data = request.POST
        filled_form = PostForm(data)
        filled_form.save()
        print("POST", data)

    post_form = PostForm(initial={'title' : 'post !!!', 'content' : 'whatever', 'author' : current_user})
    context = {'form': post_form}
    return render(request, 'add_post.html', context)


def add_category_view(request):

    # print("GET DATA", request.GET)
    # name = request.GET['name']
    # category_form = CategoryForm()
    # context = {'form': CategoryForm}
    # return render(request, 'add_category.html', context)

    if request.method == 'POST':
        data = request.POST
        filled_form = CategoryForm(data)
        filled_form.save()
        print("POST", data)

    category_form = CategoryForm()
    context = {'form': category_form}
    return render(request, 'add_category.html', context)

def posts(request):

    query = request.GET.get('query', None)
    if query:
        posts_all = Post.objects.filter(title__icontains=query)
    else:
        posts_all = Post.objects.all()

    search_form = SearchForm()

    context = {'post_list': posts_all, 'search' : search_form}
    
    return render(request, 'posts.html', context)


def profile(request):

    user_email = current_user.email

    context = {'user': current_user, 'email': user_email}

    return render(request, 'profile.html', context)


# def profile(request):

#     context = {
#         'name' : 'Yossi',
#         'hobbies' : ['sleep', 'drink water', 'eat'],
#         'gender' : 'M'
#     }

#     return render(request, 'profile_user.html', context)