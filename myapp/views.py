from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def story(request):
    return render(request, 'story.html')


def blog(request):
    return render(request, 'blog.html')


def forum(request):
    return render(request, 'forum.html')


def first_day(request):
    return render(request, 'first_day.html')


def media(request):
    return render(request, 'media.html')


def new_year(request):
    return render(request, 'new_year_favorite_menu.html')


def products(request):
    return render(request, 'products.html')


def story(request):
    return render(request, 'story.html')


def videos(request):
    return render(request, 'videos.html')


def one_week(request):
    return render(request, 'we_are_one_week_old.html')


def home_p(request):
    return render(request, 'home_p.html')
