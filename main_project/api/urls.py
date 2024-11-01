from django.urls import path, include
from . import views

urlpatterns = [
    path('get', views.getUrls),
    path('store', views.storeData),
    path('form', views.storeUrl),
    path('main', views.main),
]