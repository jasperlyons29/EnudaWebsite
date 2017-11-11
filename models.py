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


class ThirdSection(TimeStampBaseModel):
    first_icon_section = models.ForeignKey('IconSection', null=True, blank=True,
                             related_name='third_section_firsts')
    second_icon_section = models.ForeignKey('IconSection', null=True, blank=True,
                             related_name='third_section_seconds')
    third_icon_section = models.ForeignKey('IconSection', null=True, blank=True,
                             related_name='third_section_thirds')
    forth_icon_section = models.ForeignKey('IconSection', null=True, blank=True,
                             related_name='third_section_forths')