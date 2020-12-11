from django.db import models
from timestampedmodel.models import TimestampedModel

class Videos( TimestampedModel, models.Model):
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null =True)
    video = models.FileField(upload_to='videos' ,null =True,verbose_name="")
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return "{0},{1}".format(self.pk, self.first_name)

class Files(TimestampedModel, models.Model):
    title  = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True) 
    file = models.FileField(upload_to='files' ,null =True,verbose_name="")
    def __str__(self):
        return "{0},{1}".format(self.pk, self.title)

class Template( TimestampedModel, models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    video_base = models.FileField(upload_to='template' ,null =True,verbose_name="")

    def __str__(self):
        return "{0},{1}".format(self.pk, self.name)

