from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    name = models.CharField(max_length=63)
    age  = models.PositiveIntegerField()
    email= models.EmailField()
    
    def __str__(self):
        return self.name


class Question(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question')
    title   = models.CharField(max_length=255)
    body    = models.TextField()
    slug    = models.SlugField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}: {self.title[:20]}"
    
    
class Answer(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer')
    question= models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    body    = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}: {self.question.title[:20]}"
    
    
         
