from django.contrib import admin
from .models import Videos
# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display =('pk','first_name', 'last_name')

admin.site.register(Videos, VideoAdmin)