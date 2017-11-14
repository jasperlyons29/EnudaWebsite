from django.shortcuts import render
from .models import (Navigation, 
					SecondSection, 
					ThirdSection, 
					FourthSection,
					FifthSection,
					SixthSection,
					SeventhSection,
          EighthSection)


# Create your views here.
def home(request):
    second_section = SecondSection.objects.first()
    third_section = ThirdSection.objects.first()
    fourth_section = FourthSection.objects.first()
    fifth_section = FifthSection.objects.first()
    sixth_section = SixthSection.objects.first()
    seventh_section = SeventhSection.objects.first()
    eighth_section = EighthSection.objects.first()
    nav_obj = Navigation.objects.first()
    context = {'nav': nav_obj,
               'second_section': second_section,
               'third_section': third_section,
               'fourth_section': fourth_section,
               'fifth_section': fifth_section,
               'sixth_section': sixth_section,
               'seventh_section': seventh_section,
               'eighth_section': eighth_section}

    return render(request, "enuda_house_app/index.html", context)
