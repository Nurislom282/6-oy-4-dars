from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .models import Book,Author,Review

def mainpage(request: WSGIRequest):
    books = Book.objects.all()
    authors = Author.objects.all()
    reviews = Review.objects.all()
    return render(request, 'index.html', {"books": books,"authors":authors,"reviews":reviews})

def author(request: WSGIRequest):
    authors = Author.objects.all()
    return render(request,'authors.html',{'authors':authors})

def coments(request: WSGIRequest):
    reviews = Review.objects.all()
    return render(request,'coments.html',{"reviews":reviews})



