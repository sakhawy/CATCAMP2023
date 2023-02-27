from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # pssst, yes, you'll write code here :)
    path('usd_to_egp/', views.usd_to_egp, name='usd-to-egp'),
    path('live_indomie_price/', views.live_indomie_price, name='live-indomie-price')
]