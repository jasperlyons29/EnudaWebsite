from django.db import models
from . models_utils import (
    IntegerRangeField,
    image_upload_location,
    video_upload_location,
    NameTimeStampBaseModel,
    TimeStampBaseModel,
    Image,
    HighQualityImage
)


class ImageSection(TimeStampBaseModel):
    image = models.ForeignKey('Image', null=True, blank=True,
                              related_name='image_sections')
    caption = models.CharField(null=True, blank=True, max_length=300)
    chinese_caption = models.CharField(null=True, blank=True, max_length=300)
    sub_caption = models.CharField(null=True, blank=True, max_length=300)
    chinese_sub_caption = models.CharField(null=True, blank=True, max_length=300)

    def __str__(self):
        return self.image.image.name



# Create your models here.
class Navigation(NameTimeStampBaseModel):
    logo_image = models.FileField(null=True, blank=True,
                                  upload_to=video_upload_location)
    high_quality_logo_image = models.ForeignKey(HighQualityImage,
                                                null=True,
                                                blank=True,
                                                related_name="navigations")



class SecondSection(TimeStampBaseModel):
    title = models.CharField(null=True, blank=True, max_length=300)
    chinese_title = models.CharField(null=True, blank=True, max_length=300)
    header = models.TextField(null=True, blank=True)
    chinese_header = models.TextField(null=True, blank=True)
    content_one = models.TextField(null=True, blank=True)
    chinese_content_one = models.TextField(null=True, blank=True)
    content_two = models.TextField(null=True, blank=True)
    chinese_content_two = models.TextField(null=True, blank=True)
    image_section_one = models.ForeignKey('ImageSection',
                                          null=True,
                                          blank=True,
                                          related_name='image_sections_ones')
    image_section_two = models.ForeignKey('ImageSection',
                                          null=True,
                                          blank=True,
                                          related_name='image_sections_twos')
    image_section_three = models.ForeignKey('ImageSection',
                                          null=True,
                                          blank=True,
                                          related_name='image_sections_threes')
    image_section_four = models.ForeignKey('ImageSection',
                                           null=True,
                                           blank=True,
                                           related_name='background_images')


class TextSection(TimeStampBaseModel):
    content = models.TextField(null=True, blank=True)
    chinese_content = models.TextField(null=True, blank=True)
    sub_content = models.TextField(null=True, blank=True)
    chinese_sub_content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.content


class Icon(NameTimeStampBaseModel):
    caption = models.CharField(null=True, blank=True, max_length=300)
    chinese_caption = models.CharField(null=True, blank=True, max_length=300)


class IconSection(TimeStampBaseModel):
    icon = models.ForeignKey("Icon", null=True,
                             blank=True,
                             related_name="icon_sections")
    text_section_one = models.ForeignKey("TextSection",
                                         null=True,
                                         blank=True,
                                         related_name="text_section_ones")
    text_section_two = models.ForeignKey("TextSection",
                                         null=True,
                                         blank=True,
                                         related_name="text_section_twos")
    text_section_three = models.ForeignKey("TextSection",
                                         null=True,
                                         blank=True,
                                         related_name="text_section_threes")

    def __str__(self):
        return self.icon.name

class IconSectionTwo(TimeStampBaseModel):
    icon = models.ForeignKey("Icon", null=True,
                             blank=True,
                             related_name="icon_section_two_icons")
    text_section = models.ForeignKey("TextSection",
                                     null=True,
                                     blank=True,
                                     related_name="icon_section_two_text")

    def __str__(self):
        return self.icon.name


class ThirdSection(TimeStampBaseModel):
    header = models.CharField(null=True, blank=True, max_length=300)
    chinese_header = models.CharField(null=True, blank=True, max_length=300)
    first_icon_section = models.ForeignKey('IconSection', null=True, blank=True,
                             related_name='third_section_firsts')
    second_icon_section = models.ForeignKey('IconSection', null=True, blank=True,
                             related_name='third_section_seconds')
    third_icon_section = models.ForeignKey('IconSection', null=True, blank=True,
                             related_name='third_section_thirds')
    forth_icon_section = models.ForeignKey('IconSection', null=True, blank=True,
                             related_name='third_section_forths')

class FourthSection(NameTimeStampBaseModel):
    button = models.CharField(null=True, blank=True, max_length=300)
    chinese_button = models.CharField(null=True, blank=True, max_length=300)
    content = models.ForeignKey('TextSection', null=True, blank=True,
                             related_name='fourth_section_contents')
    fourth_section_pic = models.ForeignKey('Image', null=True, blank=True,
                             related_name='fourth_section_pics')

class FifthSection(TimeStampBaseModel):
    name = models.CharField(null=True, blank=True, max_length=300)
    chinese_name = models.CharField(null=True, blank=True, max_length=300)
    intro_content = models.TextField(null=True, blank=True)
    chinese_intro_content = models.TextField(null=True, blank=True)
    header_one = models.CharField(null=True, blank=True, max_length=300)
    chinese_header_one = models.CharField(null=True, blank=True, max_length=300)
    header_two = models.CharField(null=True, blank=True, max_length=300)
    chinese_header_two = models.CharField(null=True, blank=True, max_length=300)
    header_three = models.CharField(null=True, blank=True, max_length=300)
    chinese_header_three = models.CharField(null=True, blank=True, max_length=300)
    header_four = models.CharField(null=True, blank=True, max_length=300)
    chinese_header_four = models.CharField(null=True, blank=True, max_length=300)
    picture_one = models.ForeignKey('ImageSection', null=True, blank=True,
                                    related_name='fifth_section_pic_ones')
    picture_two = models.ForeignKey('ImageSection', null=True, blank=True,
                                    related_name='fifth_section_pic_twos')
    picture_three = models.ForeignKey('ImageSection', null=True, blank=True,
                                    related_name='fifth_section_pic_threes')
    picture_four = models.ForeignKey('ImageSection', null=True, blank=True,
                                    related_name='fifth_section_pic_fours')
    picture_five = models.ForeignKey('ImageSection', null=True, blank=True,
                                    related_name='fifth_section_pic_fives')
    picture_six = models.ForeignKey('ImageSection', null=True, blank=True,
                                    related_name='fifth_section_pic_sixes')

class SixthSection(NameTimeStampBaseModel):
    header = models.CharField(null=True, blank=True, max_length=300)
    chinese_header = models.CharField(null=True, blank=True, max_length=300)
    button = models.CharField(null=True, blank=True, max_length=300)
    chinese_button = models.CharField(null=True, blank=True, max_length=300)

class SeventhSection(NameTimeStampBaseModel):
    header = models.CharField(blank=True, null=True, max_length=300)
    chinese_header = models.CharField(blank=True, null=True, max_length=300)
    first_icon_section = models.ForeignKey('IconSectionTwo', null=True, blank=True,
                                           related_name='seventh_section_firsts')
    second_icon_section = models.ForeignKey('IconSectionTwo', null=True, blank=True,
                                           related_name='seventh_section_seconds')
    third_icon_section = models.ForeignKey('IconSectionTwo', null=True, blank=True,
                                           related_name='seventh_section_thirds')
    fourth_icon_section = models.ForeignKey('IconSectionTwo', null=True, blank=True,
                                           related_name='seventh_section_fourths')
    fifth_icon_section = models.ForeignKey('IconSectionTwo', null=True, blank=True,
                                           related_name='seventh_section_fifths')
    sixth_icon_section = models.ForeignKey('IconSectionTwo', null=True, blank=True,
                                           related_name='seventh_section_sixths')

class EighthSection(NameTimeStampBaseModel):
    header = models.CharField(blank=True, null=True, max_length=300)
    chinese_header = models.CharField(blank=True, null=True, max_length=300)
    quote_who_one = models.ForeignKey('TextSection', null=True, blank=True,
                                related_name = 'eighth_section_quote_who_ones')
    quote_who_two = models.ForeignKey('TextSection', null=True, blank=True,
                                related_name = 'eighth_section_quote_who_twos')
    quote_who_three = models.ForeignKey('TextSection', null=True, blank=True,
                                related_name = 'eighth_section_quote_who_threes')

class ContactSection(NameTimeStampBaseModel):
    title = models.CharField(blank=True, null=True, max_length=300)
    chinese_title = models.CharField(blank=True, null=True, max_length=300)
    address_header = models.CharField(blank=True, null=True, max_length=300)
    chinese_address_header = models.CharField(blank=True, null=True, max_length=300)
    address = models.CharField(blank=True, null=True, max_length=300)
    chinese_address = models.CharField(blank=True, null=True, max_length=300)
    email_header = models.CharField(blank=True, null=True, max_length=300)
    chinese_email_header = models.CharField(blank=True, null=True, max_length=300)
    email = models.CharField(blank=True, null=True, max_length=300)
    chinese_email = models.CharField(blank=True, null=True, max_length=300)
    

class NavBar(TimeStampBaseModel):
    home = models.CharField(blank=True, null=True, max_length=300)
    chinese_home = models.CharField(blank=True, null=True, max_length=300)
    about = models.CharField(blank=True, null=True, max_length=300)
    chinese_about = models.CharField(blank=True, null=True, max_length=300)
    services = models.CharField(blank=True, null=True, max_length=300)
    chinese_services = models.CharField(blank=True, null=True, max_length=300)
    portfolio = models.CharField(blank=True, null=True, max_length=300)
    chinese_portfolio = models.CharField(blank=True, null=True, max_length=300)
    contact = models.CharField(blank=True, null=True, max_length=300)
    chinese_contact = models.CharField(blank=True, null=True, max_length=300)



    


