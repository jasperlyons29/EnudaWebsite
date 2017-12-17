from django.contrib import admin
from .models import (
    Navigation,
    Icon,
    IconSection,
    IconSectionTwo,
    ImageSection,
    TextSection,
    SecondSection,
    ThirdSection,
    FourthSection,
    FifthSection,
    SixthSection,
    SeventhSection,
    EighthSection,
    ContactSection,
    NavBar)

from .models_utils import Image, HighQualityImage


class IconAdmin(admin.ModelAdmin):
    list_display = ['name', 'timestamp', 'updated', 'caption', 'chinese_caption']


class NavigationAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo_image', 'high_quality_logo_image',
                    'timestamp', 'updated']


class SecondSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'chinese_title', 
                    'header', 'chinese_header',
                    'content_one', 'chinese_content_one', 
                    'content_two', 'chinese_content_two',
                    'timestamp', 'updated']


class TextSectionAdmin(admin.ModelAdmin):
    list_display = ['content', 'chinese_content',
                    'sub_content', 'chinese_sub_content',
                    'timestamp', 'updated']


class IconSectionAdmin(admin.ModelAdmin):
    list_display = ['icon', 'text_section_one', 'text_section_two',
                    'text_section_three',
                    'timestamp', 'updated']

class IconSectionTwoAdmin(admin.ModelAdmin):
    list_display = ['icon', 'text_section']



class ThirdSectionAdmin(admin.ModelAdmin):
    list_display = ['header', 'chinese_header',
                    'first_icon_section', 'second_icon_section',
                    'third_icon_section', 'forth_icon_section',
                    'timestamp', 'updated']

class FourthSectionAdmin(admin.ModelAdmin):
    list_display = ['button', 'chinese_button',
                    'fourth_section_pic', 'content']

class FifthSectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'intro_content',
                    'header_one', 'chinese_header_one',
                    'header_two', 'chinese_header_two',
                    'header_three', 'chinese_header_three',
                    'header_four', 'chinese_header_four',
                    'picture_one', 'picture_two',
                    'picture_three', 'picture_four',
                    'picture_five', 'picture_six']

class SixthSectionAdmin(admin.ModelAdmin):
    list_display = ['header', 'chinese_header', 
                    'button', 'chinese_button']

class SeventhSectionAdmin(admin.ModelAdmin):
    list_display = ['header', 'chinese_header',
                    'first_icon_section', 'second_icon_section',
                    'third_icon_section', 'fourth_icon_section',
                    'fifth_icon_section', 'sixth_icon_section']

class EighthSectionAdmin(admin.ModelAdmin):
    list_display = ['header', 'chinese_header', 
                    'quote_who_one', 'quote_who_two', 'quote_who_three']

class ContactSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'chinese_title',
                    'address_header', 'chinese_address_header',
                    'address', 'chinese_address',
                    'email_header', 'chinese_email_header',
                    'email', 'chinese_email']

class NavBarAdmin(admin.ModelAdmin):
    list_display = ['home', 'chinese_home',
                    'about', 'chinese_about',
                    'services', 'chinese_services',
                    'portfolio', 'chinese_portfolio',
                    'contact', 'chinese_contact']



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
admin.site.register(FourthSection, FourthSectionAdmin)
admin.site.register(FifthSection, FifthSectionAdmin)
admin.site.register(SixthSection, SixthSectionAdmin)
admin.site.register(SeventhSection, SeventhSectionAdmin)
admin.site.register(EighthSection, EighthSectionAdmin)
admin.site.register(ContactSection, ContactSectionAdmin)
admin.site.register(NavBar, NavBarAdmin)
admin.site.register(TextSection, TextSectionAdmin)
admin.site.register(IconSection, IconSectionAdmin)
admin.site.register(IconSectionTwo, IconSectionTwoAdmin)