from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TodoForm
from .models import Todo, Category


# Create your views here.

@login_required
def categories(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})


# @login_required
# def todo(request):
#     if request.method == "POST":
#         title = request.POST["title"]
#         details = request.POST["details"]
#         deadline_date = request.POST["deadline_date"]
#         category = request.POST["category"]

#         todo = Todo(
#             title=title,
#             details=details,
#             deadline_date=deadline_date,
#             category=category,
#         )
#         todo.save()

#         return redirect("display_todos")

#     else:
#         categories = Category.objects.all()
#         return render(request, "todo/todo.html", {"categories": categories})

@login_required
def todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("display_todos")
    else:
        form = TodoForm()
    
    return render(request, "todo/todo.html", {"form": form})


@login_required
def display_todos(request):
    todos = Todo.objects.all()
    return render(request, "todo/display_todos.html", {"todos": todos})