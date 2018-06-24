from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # User search from API
    path('user_search/',  views.user_search.as_view()),
    # Storing data using API with managing unique contraints
    path('add_user/',  views.add_user.as_view()),

]