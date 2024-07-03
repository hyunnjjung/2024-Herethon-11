from django.contrib import admin

from .models import Question, Answer, Tag,Rating
# Register your models here.
admin.site.register(Question) #모델 admin에 등록
admin.site.register(Answer) #모델 admin에 등록
admin.site.register(Rating) #모델 admin에 등록


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(Tag, TagAdmin)