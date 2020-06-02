from django.urls import path
from . import views

urlpatterns = [path("",views.index,name="index"),
path("home",views.index,name='home'),
path("<int:image_id>",views.image,name='image'),
path("cartt",views.cartt,name="cartt"),
path("book",views.book,name='book')]