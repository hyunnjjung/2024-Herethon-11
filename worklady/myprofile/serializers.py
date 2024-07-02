from rest_framework import serializers
from rest_framework.serializers import ModelSerializer 
from .models import Profile, Education, Career

class EducationSerializer(ModelSerializer): 
    class Meta:
        model = Education
        fields = ['id', 'school', 'grade']
        
class CareerSerializer(ModelSerializer):
    
    class Meta:
        model = Career
        fields = ['id', 'department', 'category']
        
# class CertificateSerializer(ModelSerializer):
#     class Meta:
#         model = Certificate
#         fields = ['certificate']

class ProfileSerializer(serializers.ModelSerializer):
    school = serializers.CharField(write_only=True, required=False)
    grade = serializers.ChoiceField(choices=Education.GRADES, write_only=True, required=False)
    education = EducationSerializer(many=True, read_only=True)
    
    department = serializers.CharField(write_only=True, required=False)
    category = serializers.ChoiceField(choices=Career.CATEGORIES, write_only=True, required=False)
    career = CareerSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'my_image', 'short_intro', 
                  'school', 'grade', 'education',  
                  'department', 'category', 'career', 
                  'interest', 'certificate', 
                  'current_job', 'introduce']

    def create(self, validated_data):
        school = validated_data.pop('school', None)
        grade = validated_data.pop('grade', None)
        educations_data = validated_data.pop('educations', [])
        department = validated_data.pop('department', None)
        category = validated_data.pop('category', None)
        careers_data = validated_data.pop('careers', [])
        profile = Profile.objects.create(**validated_data)
        
        if school and grade:
            education, created = Education.objects.get_or_create(school=school, grade=grade)
            profile.education.add(education)

        for education_data in educations_data:
            education = Education.objects.get_or_create(**education_data)
            profile.education.add(education)
        
        if department and category:
            career = Career.objects.get_or_create(department=department, category=category)
            profile.career.add(career)

        for career_data in careers_data:
            career = Career.objects.get_or_create(**career_data)
            profile.career.add(career)
        
        return profile