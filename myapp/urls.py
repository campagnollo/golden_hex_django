"""
This module defines URL patterns for the Django application.

Each URL pattern is associated with a view function from the views module.
"""

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
    path("dom", views.dom, name="dom"),
    path("exciting-news-we-moved-expanded", views.exciting_news_we_moved_expanded, name="exciting-news-we-moved"
                                                                                        "-expanded"),
    path("new_year_favorite_menu", views.new_year_favorite_menu, name="new_year_favorite_menu"),
    path("we_are_one_week_old", views.we_are_one_week_old, name="we_are_one_week_old"),
    path("first_day", views.first_day, name="first_day")
]
