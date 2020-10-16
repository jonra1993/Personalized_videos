from django.db import models
from timestampedmodel.models import TimestampedModel
from apps.files.models import Videos, Files


class Campaign(TimestampedModel, models.Model):
    campaign = models.CharField(max_length=40, blank=True, null =True)
    videos = models.ManyToManyField(Videos,related_name="videos_campaign")
    csv_file = models.ForeignKey(Files, on_delete = models.CASCADE,related_name= 'file_csv', )


