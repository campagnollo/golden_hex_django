from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("story", views.story, name="story"),
    path("blog", views.blog, name="blog"),
    path("forum", views.forum, name="forum"),
    path("first_day", views.first_day, name="first_day"),
    path("media", views.media, name="media"),
    path("new_year", views.new_year, name="new_year"),
    path("products", views.products, name="products"),
    path("story", views.story, name="story"),
    path("videos", views.videos, name="videos"),
    path("one_week", views.one_week, name="one_week"),
    path("home_russian", views.home_p, name="home_p"),
]

