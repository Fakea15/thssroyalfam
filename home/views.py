from django.shortcuts import render
from datetime import date
from django.views.generic import CreateView
from .forms import CommentForm
from .models import Comment

copyright_var = date.today()
x = copyright_var.year
CR = "Mama Chhangte"
Assistant_CR = "Awmawmi Chhakchuak"
the_programmer = "The Web Developer"

def homeView(request):
    class_zat = 62
    return render(request, 'home.html', {
        "copyright_year": x,
        "class_zat": class_zat,
    })

def contact(request):
    return render(request, 'contact.html', {
        "copyright_year": x,
        "CR": CR,
        "Assistant_CR": Assistant_CR,
        "owner": the_programmer,
    })

def about_page(request):
    return render(request, 'about.html', {
        "CR": CR,
        "Assistant_CR": Assistant_CR,
        "owner": the_programmer,
    })

def thlalak(request):
    return render(request, 'thlalak.html', {
        "CR": CR,
        "Assistant_CR": Assistant_CR,
        "owner": the_programmer,
    })

class CommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment.html'

def successful(request):
    return render(request, 'success.html', {})


