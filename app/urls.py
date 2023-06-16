from django.urls import path
from app.views import *
urlpatterns=[
    path('wish/',wish,name='wish'),
]