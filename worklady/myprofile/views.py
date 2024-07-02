from django.shortcuts import render
# from .models import Profile, Education, Career, Certificate
from .models import Profile
# from .serializers import ProfileSerializer, EducationSerializer, CareerSerializer, CertificateSerializer
from .serializers import ProfileSerializer
from rest_framework.viewsets import ModelViewSet 

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer