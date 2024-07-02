from django.shortcuts import render
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.viewsets import ModelViewSet 

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def perform_create(self, serializer): 
        serializer.save(username = self.request.user)