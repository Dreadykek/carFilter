from django.shortcuts import render
from django.views.generic import ListView
from app.models import Car
from django.db.models import Q

# Create your views here.

class CarList(ListView):
    model = Car
    template_name = 'car_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        get_params = self.request.GET.dict()

        if get_params.get('q'):
            qs = qs.filter(Q(producer=get_params.get('q')))

        if get_params.get('w'):
            qs = qs.filter(Q(car_model=get_params.get('w')))

        if get_params.get('q') and get_params.get('w'):
            qs = qs.filter(Q(producer=get_params.get('q')) & Q(car_model=get_params.get('w')))

        return qs
