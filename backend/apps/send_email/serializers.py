from rest_framework import serializers
from apps.files.models import Videos


class EmailSerializer(serializers.Serializer):
    class Meta:
        model= Videos
        fields = ['first_name','last_name','email','video']

    def to_representation(self,instance):
        return {
            "email_address": instance.email,
            "status": "subscribed",
            "merge_fields": {
                "FNAME": instance.first_name,
                "LNAME": instance.last_name,
                "URLVIDEO": instance.video.url
            }
        
        }
