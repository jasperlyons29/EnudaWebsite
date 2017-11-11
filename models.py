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

def video_upload_location(instance, filename):
	return "logos/{}".format(filename)

# Create your models here.
class Navigation(NameTimeStampBaseModel):
	logo_image = models.FileField(null=True, blank=True, upload_to=video_upload_location)
	high_quality_logo_image = models.ForeignKey(HighQualityImage, null=True, blank=True, related_name="navigations")

class TextPieceAbout(NameTimeStampBaseModel):
	text = models.CharField(null=True, blank=True, max_length=300)

	def __str__(self):
		return self.name

class TextPieceServices(NameTimeStampBaseModel):
    text = models.CharField(null=True, blank=True, max_length=300)

    def __str__(self):
        return self.name

