from django.contrib import admin
from .models import Campaign

class CampaignAdmin(admin.ModelAdmin):
    list_display=('pk','campaign')

admin.site.register(Campaign, CampaignAdmin)