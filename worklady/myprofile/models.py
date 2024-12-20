from django.db import models
from signup.models import CustomUser   
    
class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    my_image = models.ImageField(verbose_name="프로필사진", upload_to='profile_image')
    short_intro = models.CharField(verbose_name="한줄소개", max_length=200)
    interest = models.CharField(verbose_name="대표관심분야", max_length=200)
    current_job = models.CharField(verbose_name="현재관심분야", max_length=200)
    introduce = models.TextField(verbose_name="소개", default='') 
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    
    def __str__(self):
        return self.short_intro
    
class Education(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    school = models.CharField(verbose_name="학교명", max_length=200, null=True, blank=True)
    GRADES = [
        ('1학년', '1학년'),
        ('2학년', '2학년'),
        ('3학년', '3학년'),
        ('4학년 이상', '4학년 이상'),
        ('졸업', '졸업'),
    ]
    grade = models.CharField(verbose_name="학년", max_length=15, choices=GRADES, null=True, blank=True)
    def __str__(self):
        return self.school
    
class Career(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    department = models.CharField(verbose_name="부서", max_length=200, null=True, blank=True)
    CATEGORIES = [
        ('전 근무지', '전 근무지'),
        ('현 근무지', '현 근무지'),
        ('인턴', '인턴'),
    ]
    category = models.CharField(verbose_name="유형", max_length=15, choices=CATEGORIES, null=True, blank=True)
    def __str__(self):
        return self.department
    
class Certificate(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    certificate = models.CharField(verbose_name="자격증", max_length=300, blank=True, null=True)
    def __str__(self):
        return self.certificate 