from django.shortcuts import render
from .models import Profile, Education, Career, Certificate
from django.db.models import Q
from .serializers import ProfileSerializer, EducationSerializer, CareerSerializer, CertificateSerializer
from rest_framework.viewsets import ModelViewSet 
from rest_framework.decorators import action
from rest_framework.response import Response

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def perform_create(self, serializer): 
        serializer.save(username=self.request.user)
        
    # 프로필 검색
    def get_queryset(self):
        queryset = Profile.objects.all()
        search_keyword = self.request.GET.get('q', '')

        if search_keyword:
            queryset = queryset.filter(
                Q(username__name__icontains=search_keyword) |
                Q(current_job__icontains=search_keyword)
            )
        return queryset

    # 검색테스트
    @action(detail=False, methods=['get'], url_path='list-view')
    def list_view(self, request):
        profiles = self.get_queryset()
        return render(request, 'profile_list.html', {'profiles': profiles})
    
class EducationViewSet(ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
    def perform_create(self, serializer): 
        serializer.save(username=self.request.user)
    
    def get_queryset(self, **kwargs):
        id = self.kwargs['profile_id']
        return self.queryset.filter(profile=id)

class CareerViewSet(ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer
    
    def perform_create(self, serializer): 
        serializer.save(username=self.request.user)
        
    def get_queryset(self, **kwargs):
        id = self.kwargs['profile_id']
        return self.queryset.filter(profile=id)

class CertificateViewSet(ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    
    def perform_create(self, serializer): 
        serializer.save(username=self.request.user)
    
    def get_queryset(self, **kwargs):
        id = self.kwargs['profile_id']
        return self.queryset.filter(profile=id)
