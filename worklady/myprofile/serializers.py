from rest_framework import serializers
from rest_framework.serializers import ModelSerializer 
from .models import Profile, Education, Career, Certificate
from signup.models import CustomUser

class EducationSerializer(ModelSerializer): 
    username = serializers.ReadOnlyField(source = 'username.name') 
    class Meta:
        model = Education
        fields = ['id', 'school', 'grade', 'profile', 'username']
        
class CareerSerializer(ModelSerializer):
    username = serializers.ReadOnlyField(source = 'username.name') 
    class Meta:
        model = Career
        fields = ['id', 'department', 'category', 'profile', 'username']
        
class CertificateSerializer(ModelSerializer):
    username = serializers.ReadOnlyField(source = 'username.name') 
    class Meta:
        model = Certificate
        fields = ['id', 'certificate', 'profile', 'username']

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source = 'username.name') 

    class Meta:
        model = Profile
        fields = ['id', 'my_image', 'short_intro', 
                  'interest', 'current_job', 'introduce', 'username', 'created_at']
        