from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # directs user to homepage, then tells site to looj at the index function in the view.py file
    path('post/<str:pk>', views.post, name='post'), # adds /pk after post in the url
]