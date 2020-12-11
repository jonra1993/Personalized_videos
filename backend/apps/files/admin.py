from django.contrib import admin
from .models import Videos, Files, Template
# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display =('pk','first_name', 'last_name')

class FileAdmin(admin.ModelAdmin):
    list_display = ('pk','title')

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('pk','name')

admin.site.register(Videos, VideoAdmin)
admin.site.register(Files, FileAdmin)
admin.site.register(Template, TemplateAdmin)

