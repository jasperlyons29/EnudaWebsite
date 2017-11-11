from django.shortcuts import render
from .models import Navigation, SecondSection, ThirdSection


# Create your views here.
def home(request):
    second_section = SecondSection.objects.first()
    third_section = ThirdSection.objects.first()
    nav_obj = Navigation.objects.first()
    context = {'nav': nav_obj,
               'second_section': second_section,
               'third_section': third_section}

    return render(request, "enuda_house_app/index.html", context)
