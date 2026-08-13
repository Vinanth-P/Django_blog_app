from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        "author":"john",
        "title":"first blog",
        "content":"dont know",
        "date":"today"
    },
    {
        "author":"not john",
        "title":"second blog",
        "content":"still dont know",
        "date":"today"
    },
]

def home(request):
    context={
        "posts":posts
    }
    return render(request,"blog/home.html",context)

def about(request):
    return render(request,"blog/about.html")