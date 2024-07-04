from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ProfileModelForm, EducationModelForm, CareerModelForm, CertificateModelForm
from .models import *
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

#프로필 보기
def profile_list(request):
    # profiles 쿼리셋을 가져올 때 관련된 Education, Career, Certificate 정보도 함께 가져오기
    profiles = Profile.objects.all().prefetch_related('education_set', 'career_set', 'certificate_set').order_by('-created_at')
    return render(request, "profile_list.html", {'profiles': profiles})

# <a href="{% url 'user_detail' %}">View My Profile</a> 이거 입력하면 내 프로필로 이동
@login_required
def user_detail(request):
    # 현재 로그인한 사용자의 ID를 기반으로 프로필을 가져옵니다.
    profile = get_object_or_404(Profile, username=request.user)
    # 관련된 Education, Career, Certificate 데이터를 prefetch_related로 가져옵니다.
    profile = Profile.objects.prefetch_related('education_set', 'career_set', 'certificate_set').get(username=request.user)

    return render(request, "user_detail.html", {
        "profile": profile,
        "educations": profile.education_set.all(),
        "careers": profile.career_set.all(),
        "certificates": profile.certificate_set.all(),
    })

# 프로필 등록 생성
def create_profile1(request):
    if request.method == 'POST':
        profile_form = ProfileModelForm(request.POST, request.FILES)
        education_form = EducationModelForm(request.POST)
        career_form = CareerModelForm(request.POST)
        certificate_form = CertificateModelForm(request.POST)

        # 모든 폼이 유효한 경우에만 저장
        if profile_form.is_valid() and education_form.is_valid() and career_form.is_valid() and certificate_form.is_valid:
            new_profile = profile_form.save()
            # Profile 인스턴스와 연관된 Education과 Career 인스턴스 생성
            new_education = education_form.save(commit=False)
            new_education.profile = new_profile
            new_education.save()

            new_career = career_form.save(commit=False)
            new_career.profile = new_profile
            new_career.save()
            
            new_certificate = certificate_form.save(commit=False)
            new_certificate.profile = new_profile
            new_certificate.save()
            return redirect('profile_list') #내 프로필 확인으로 이동
    else:
        profile_form = ProfileModelForm()
        education_form = EducationModelForm()
        career_form = CareerModelForm()
        certificate_form = CertificateModelForm()

    return render(request, 'create_profile1.html', {
        'profile_form': profile_form,
        'education_form': education_form,
        'career_form': career_form,
        'certificate_form': certificate_form,
    }) #form 객체를 html에 찍어 보냄 
 
#하나의 프로필 조회
def profile_detail(request, profile_id):
    # prefetch_related를 사용하여 연관된 모든 데이터를 함께 가져옵니다.
    profile = get_object_or_404(Profile.objects.prefetch_related('education_set', 'career_set', 'certificate_set'), pk=profile_id)

    return render(request, "profile_detail.html", {
        "profile": profile,
        "educations": profile.education_set.all(),
        "careers": profile.career_set.all(),
        "certificates": profile.certificate_set.all(),
    })

# 프로필 수정
def profile_update(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    educations = Education.objects.filter(profile=profile)
    careers = Career.objects.filter(profile=profile)
    certificates = Certificate.objects.filter(profile=profile)

    if request.method == 'POST':
        profile_form = ProfileModelForm(request.POST, request.FILES, instance=profile)
        education_forms = [EducationModelForm(request.POST, instance=education, prefix=str(education.id)) for education in educations]
        career_forms = [CareerModelForm(request.POST, instance=career, prefix=str(career.id)) for career in careers]
        certificate_forms = [CertificateModelForm(request.POST, instance=certificate, prefix=str(certificate.id)) for certificate in certificates]

        forms_valid = all([profile_form.is_valid()] + [form.is_valid() for form in education_forms + career_forms + certificate_forms])

        if forms_valid:
            profile_form.save()
            for form in education_forms + career_forms + certificate_forms:
                form.save()
            return redirect('profile_list')
    else:
        profile_form = ProfileModelForm(instance=profile)
        education_forms = [EducationModelForm(instance=education, prefix=str(education.id)) for education in educations]
        career_forms = [CareerModelForm(instance=career, prefix=str(career.id)) for career in careers]
        certificate_forms = [CertificateModelForm(instance=certificate, prefix=str(certificate.id)) for certificate in certificates]

    context = {
        'profile_form': profile_form,
        'education_forms': education_forms,
        'career_forms': career_forms,
        'certificate_forms': certificate_forms,
        'profile_id': profile_id
    }
    return render(request, 'profile_update.html', context)

#검색기능
def profile_list(request):
    search_keyword = request.GET.get('q', '') # 검색어 가져오기
    # profiles 쿼리셋을 가져올 때 관련된 Education, Career, Certificate 정보도 함께 가져오기
    if search_keyword:
        profiles = Profile.objects.prefetch_related('education_set', 'career_set', 'certificate_set').filter(
            Q(username__name__icontains=search_keyword) |
            Q(current_job__icontains=search_keyword)
        ).order_by('-created_at')
    else:
        profiles = Profile.objects.all().prefetch_related('education_set', 'career_set', 'certificate_set').order_by('-created_at')
    
    return render(request, "profile_list.html", {'profiles': profiles})