from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404, redirect
from . import models


def index(request):
    videos = models.VideoNews.objects.all()
    news = models.News.objects.all()
    first_new = models.News.objects.last()
    humans = models.Human.objects.all()
    contact = models.Contact.objects.all()
    context = {
        'videos' : videos,
        'news' : news,
        'first_new' : first_new,
        'humans' :humans,
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method =='POST':
        f_name = request.POST['f_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        message = request.POST['message']
        
        
        models.Contact.objects.create(
            f_name = f_name,
            email = email,
            phone_number = phone_number,
            message = message
            
        )

    context = {
        'contact' : contact
    }
    return render(request, 'contact.html')


def news(request, id=0):
    try:
        news = models.News.objects.get(id=id)
    except models.News.DoesNotExist:
        news = models.News.objects.last()
    
    context = {
        'news': news
    }
    return render(request, 'news.html', context)

def about(request):
    return render(request, 'about.html')
