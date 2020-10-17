from rest_framework import serializers
from .models import Campaign

class FilePostSerializer(serializers.Serializer):
    csv_file = serializers.FileField()
    campaign = serializers.CharField()

class FileGetSerializer(serializers.ModelSerializer):
    class Meta:      
        model = Campaign
        fields =('pk','campaign','csv_file')  
    
class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields =['pk',]  

class CreateGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields =('pk','videos','csv_file')  
