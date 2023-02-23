from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # pssst, yes, you'll write code here :)
]