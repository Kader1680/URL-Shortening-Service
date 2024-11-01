from django.urls import path, include
from . import views

urlpatterns = [
    path('get', views.getData),
    path('store', views.storeData),
    path('form', views.form),
    path('main', views.main),
]