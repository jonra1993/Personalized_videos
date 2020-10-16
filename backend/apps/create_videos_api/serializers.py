from rest_framework import serializers
from .models import Campaign

class FilePostSerializer(serializers.Serializer):
    csv_file = serializers.FileField()
    name = serializers.CharField()

class FileGetSerializer(serializers.ModelSerializer):
    class Meta:      
        model = Campaign
        fields =('pk','campaign','csv_file')  
    
    
