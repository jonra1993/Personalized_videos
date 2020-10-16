from django.contrib import admin
from .models import Videos, Files
# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display =('pk','first_name', 'last_name')

class FileAdmin(admin.ModelAdmin):
    list_display = ('pk','title')

admin.site.register(Videos, VideoAdmin)
admin.site.register(Files, FileAdmin)

