from rest_framework import serializers
from .models import Question, Answer


class PersonSerial(serializers.ModelSerializer):
    name = serializers.CharField()
    age  = serializers.IntegerField()


class QuestionSerial(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    
    class Meta:
        model = Question
        fields = "__all__"
    
    def get_answers(self,obj):
        result = obj.answer.all()
        return AnswerSerial(instance=result, many=True).data
        
class AnswerSerial(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        
        