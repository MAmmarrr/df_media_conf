from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('',views.index,name='index'),
    path('add_item',views.save_item,name='add_item'),
]
