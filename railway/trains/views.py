from django.shortcuts import render
from .models import Train,Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, "trains/index.html",{
        "trains":Train.objects.all()
    })

def train(request,train_id):
    train=Train.objects.get(pk=train_id)
    return render(request, "trains/train.html",{
        "train":train,
        "passengers":train.passengers.all(),
        "non_passengers":Passenger.objects.exclude(trains=train).all()
    })

def book(request,train_id):
     if request.method=="POST":
        train=Train.objects.get(pk=train_id)
        passenger=Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.trains.add(train)
        return HttpResponseRedirect(reverse("train",args=(train_id,)))


