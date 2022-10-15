from django.contrib import admin
from .models import Train,Station,Passenger
# Register your models here.
class TrainAdmin(admin.ModelAdmin):
       list_display=("id","origin","destination","duration") 

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=("trains",)
admin.site.register(Station)
admin.site.register(Train,TrainAdmin)
admin.site.register(Passenger,PassengerAdmin)

