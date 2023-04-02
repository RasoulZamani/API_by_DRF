from rest_framework import serializers
from .models import Question, Answer


class PersonSerial(serializers.ModelSerializer):
    name = serializers.CharField()
    age  = serializers.IntegerField()


class QuestionSerial(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
    
        
class AnswerSerial(serializers.Serializer):
    class Meta:
        model = Answer
        fields = '__all__'
        
        