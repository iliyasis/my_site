from django.urls import path
from index.views import *

urlpatterns = [
    path("", home, name="home"),
    path("blog/", blog, name="blog"),
    path("contact/", contact, name="contact"),
]