from django.contrib import admin
from app.models import Car

# Register your models here.
@admin.register(Car)
class PostCar(admin.ModelAdmin):
    pass
