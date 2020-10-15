from django.db import models
from timestampedmodel.models import TimestampedModel

class Videos( TimestampedModel, models.Model):
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null =True)
    video = models.FileField( null =True,verbose_name="")

    def __str__(self):
        return "{0},{1}".format(self.pk, self.first_name)
