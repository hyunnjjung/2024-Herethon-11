
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from signup.models import CustomUser
from myprofile.models import Profile


class MentorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add other mentor-specific fields here

class Chat_Question(models.Model):
    question_text = models.TextField()
    asker = models.ForeignKey(CustomUser, related_name='asked_questions', on_delete=models.CASCADE)
    mentor = models.ForeignKey(MentorProfile, related_name='questions', on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
    is_answered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_declined = models.BooleanField(default=False)

    def __str__(self):
        return f'[{self.id}]'


class Chat_Answer(models.Model):
    question = models.ForeignKey(Chat_Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    answered_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'[{self.id}]'

class Evaluation(models.Model):
    answer = models.OneToOneField(Chat_Answer, on_delete=models.CASCADE)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)



class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/question/tag/{self.slug}/'



class Question(models.Model):
    title = models.CharField(max_length=50) #글의 제목
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    answered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[{self.id}] {self.title}'

class Answer(models.Model):
    question = models.ForeignKey(to=Question, related_name='answers', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)  # Rating value (from 1 to 5)
    
    def __str__(self):
        return f'[{self.id}] {self.content}'
    

    def average_rating(self):
        ratings = self.ratings.all()  # related_name인 'ratings'를 사용하여 평점을 가져옵니다.
        if ratings.exists():
            return ratings.aggregate(models.Avg('value'))['value__avg']
        return 0

class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    answer = models.ForeignKey(to=Answer, related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('user', 'answer')

    def __str__(self):
        return f'Rating: {self.value} by {self.user} for Answer {self.answer.id}'



