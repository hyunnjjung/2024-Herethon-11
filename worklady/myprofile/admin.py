from django.contrib import admin
from .models import Profile, Education, Career

admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Career)
# admin.site.register(Certificate)