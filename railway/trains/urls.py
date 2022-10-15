from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("<int:train_id>",views.train,name="train"),
    path("<int:train_id>/book",views.book,name="book")
]