from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'CoreySK',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'CoreySK',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'September 10, 2018'
    },
    {
        'author': 'CoreySK',
        'title': 'Blog post 3',
        'content': 'Third post content',
        'date_posted': 'October 15, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

# def about(request):
#     return HttpResponse('<h1> Blog About</h1><p>This page contains information about the blog.</p>')
