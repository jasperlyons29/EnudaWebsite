from django.contrib import admin
from .models import (
    Navigation,
    Icon,
    IconSection,
    ImageSection,
    TextSection,
    SecondSection,
    ThirdSection)
from .models_utils import Image, HighQualityImage


class IconAdmin(admin.ModelAdmin):
    list_display = ['name', 'timestamp', 'updated', 'caption']


class NavigationAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo_image', 'high_quality_logo_image',
                    'timestamp', 'updated']


class SecondSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'header', 'content_one',
                    'content_two',
                    'timestamp', 'updated']


class TextSectionAdmin(admin.ModelAdmin):
    list_display = ['content', 'sub_content', 'timestamp', 'updated']


class IconSectionAdmin(admin.ModelAdmin):
    list_display = ['icon', 'text_section_one', 'text_section_two',
                    'text_section_three',
                    'timestamp', 'updated']



class ThirdSectionAdmin(admin.ModelAdmin):
    list_display = ['first_icon_section', 'second_icon_section',
                    'third_icon_section', 'forth_icon_section',
                    'timestamp', 'updated']


class ImageSectionAdmin(admin.ModelAdmin):
    list_display = ['image', 'caption', 'sub_caption',
                    'timestamp', 'updated']


class ImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'name',
                    'timestamp', 'updated']


class HighQualityImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'name', 'timestamp', 'updated']


admin.site.register(Navigation, NavigationAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(HighQualityImage, HighQualityImageAdmin)
admin.site.register(ImageSection, ImageSectionAdmin)
admin.site.register(SecondSection, SecondSectionAdmin)
admin.site.register(Icon, IconAdmin)
admin.site.register(ThirdSection, ThirdSectionAdmin)
admin.site.register(TextSection, TextSectionAdmin)
admin.site.register(IconSection, IconSectionAdmin)