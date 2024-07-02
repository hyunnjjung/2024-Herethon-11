from django.db import models
# from django.contrib.auth.models import CustomUser

class Education(models.Model):
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
    department = models.CharField(verbose_name="부서", max_length=200, null=True, blank=True)
    CATEGORIES = [
        ('전 근무지', '전 근무지'),
        ('현 근무지', '현 근무지'),
        ('인턴', '인턴'),
    ]
    category = models.CharField(verbose_name="유형", max_length=15, choices=CATEGORIES, null=True, blank=True)
    def __str__(self):
        return self.department
    
class Profile(models.Model):
    #회원가입시 본인의 이름 불러오기 User table에서
    # username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    my_image = models.ImageField(verbose_name="프로필사진", upload_to='profile_image')
    short_intro = models.CharField(verbose_name="한줄소개", max_length=200)
    #education 테이블과 join
    education = models.ManyToManyField(Education, verbose_name="학력", blank=True, null=True,)
    #career 테이블과 join - 필수 아님
    career = models.ManyToManyField(Career, verbose_name="경력", blank=True, null=True,)
    # 자격증도 여러개 추가 가능 - 필수 아님 / related_name : Django의 ORM에서 반대 방향의 관계를 참조할 때 사용할 이름을 정의
    # certificates = models.ManyToManyField("Certificate", verbose_name="자격증", null=True, blank=True)
    certificate = models.CharField(verbose_name="자격증", max_length=300, blank=True, null=True)
    interest = models.CharField(verbose_name="대표관심분야", max_length=200)
    current_job = models.CharField(verbose_name="현재관심분야", max_length=200)
    introduce = models.TextField(verbose_name="소개", default='') 
    
    def __str__(self):
        return self.introduce

# class Certificate(models.Model):
#     # profile = models.ForeignKey(Profile, related_name='certificates', on_delete=models.CASCADE)
#     certificate = models.CharField(verbose_name="자격증", max_length=300, blank=True, null=True)
#     def __str__(self):
#         return self.certificate    