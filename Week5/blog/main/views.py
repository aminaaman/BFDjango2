from django.shortcuts import render

# Create your views here.

def returnBlog(request):
    return render(request, 'feed.html')
