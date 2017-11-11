from django.shortcuts import render
from .models import Navigation
from .models import TextPieceAbout
from .models import TextPieceServices

# Create your views here.
def home(request):
	'kk'

	who_we_are = TextPieceAbout.objects.all()[0]
	who_we_are_detail_left = TextPieceAbout.objects.all()[1]
	who_we_are_detail_right = TextPieceAbout.objects.all()[2]
	
	curric_tagline = TextPieceServices.objects.all()[0]
	curric_detail_1 = TextPieceServices.objects.all()[1]
	curric_detail_2 = TextPieceServices.objects.all()[2]
	
	nav_obj = Navigation.objects.first()
	
	context = {'nav': nav_obj, 
			   'who_we_are': who_we_are,
			   'who_we_are_detail_left': who_we_are_detail_left,
			   'who_we_are_detail_right': who_we_are_detail_right,
 			   'curric_tagline': curric_tagline,
			   'curric_detail_1': curric_detail_1,
			   'curric_detail_2': curric_detail_2
		}

	return render(request, "enuda_house_app/index.html", context)
