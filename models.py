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
    sub_caption = models.CharField(null=True, blank=True, max_length=300)

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
    header = models.TextField(null=True, blank=True)
    content_one = models.TextField(null=True, blank=True)
    content_two = models.TextField(null=True, blank=True)
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


class TextSection(TimeStampBaseModel):
    content = models.TextField(null=True, blank=True)
    sub_content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.content


class Icon(NameTimeStampBaseModel):
    caption = models.CharField(null=True, blank=True, max_length=300)


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
    first_icon_section = models.ForeignKey('IconSection', null=True, blank=True,
                             related_name='third_section_firsts')
    second_icon_section = models.ForeignKey('IconSection', null=True, blank=True,
                             related_name='third_section_seconds')
    third_icon_section = models.ForeignKey('IconSection', null=True, blank=True,
                             related_name='third_section_thirds')
    forth_icon_section = models.ForeignKey('IconSection', null=True, blank=True,
                             related_name='third_section_forths')

class FourthSection(NameTimeStampBaseModel):
    content = models.ForeignKey('TextSection', null=True, blank=True,
                             related_name='fourth_section_contents')
    fourth_section_pic = models.ForeignKey('Image', null=True, blank=True,
                             related_name='fourth_section_pics')

class FifthSection(TimeStampBaseModel):
    name = models.CharField(null=True, blank=True, max_length=300)
    intro_content = models.TextField(null=True, blank=True)
    header_one = models.CharField(null=True, blank=True, max_length=300)
    header_two = models.CharField(null=True, blank=True, max_length=300)
    header_three = models.CharField(null=True, blank=True, max_length=300)
    header_four = models.CharField(null=True, blank=True, max_length=300)

class SixthSection(NameTimeStampBaseModel):
    header = models.CharField(null=True, blank=True, max_length=300)
    button = models.CharField(null=True, blank=True, max_length=300)

class SeventhSection(NameTimeStampBaseModel):
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
    quote_who_one = models.ForeignKey('TextSection', null=True, blank=True,
                                related_name = 'eighth_section_quote_who_ones')
    quote_who_two = models.ForeignKey('TextSection', null=True, blank=True,
                                related_name = 'eighth_section_quote_who_twos')
    quote_who_three = models.ForeignKey('TextSection', null=True, blank=True,
                                related_name = 'eighth_section_quote_who_threes')
    


