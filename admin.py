from django.contrib import admin
from .models import Navigation
from .models import TextPieceAbout
from .models import TextPieceServices
from .models_utils import Image, HighQualityImage

# Register your models here.

class NavigationAdmin(admin.ModelAdmin):
	list_display = ['name', 'logo_image', 'high_quality_logo_image']

class TextPieceAboutAdmin(admin.ModelAdmin):
	list_display = ['name', 'text']

class TextPieceServicesAdmin(admin.ModelAdmin):
	list_display = ['name', 'text']


class ImageAdmin(admin.ModelAdmin):
	list_display = ['image', 'name']


class HighQualityImageAdmin(admin.ModelAdmin):
	list_display = ['image', 'name']


admin.site.register(Navigation, NavigationAdmin)
admin.site.register(TextPieceAbout, TextPieceAboutAdmin)
admin.site.register(TextPieceServices, TextPieceServicesAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(HighQualityImage, HighQualityImageAdmin)