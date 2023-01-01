from django.db import models

# Create your models here.
class ImgProject(models.Model):
    title = models.CharField(max_length=45, blank=True, null=True)
    real_img = models.ImageField(null=True, blank=True)
    thum_img = models.ImageField(null=True, blank=True)
    medium_img = models.ImageField(null=True, blank=True)
    large_img = models.ImageField(null=True, blank=True)
    gray_img = models.ImageField(null=True, blank=True)

