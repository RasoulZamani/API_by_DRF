from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Answer, Question
from .serializers import PersonSerial, QuestionSerial, AnswerSerial
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class HomeView(APIView): 
    permission_classes = [IsAuthenticated,]
    
    def get(self, request):
        #name = request.query_params['name']
        persons = Person.objects.all()
        serial_pers = PersonSerial(instance=persons, many=True)
        return Response(data=serial_pers.data)

    
    def post(self, request):
        name = request.data['name']
        return Response({'greating':name}) 
    
class QuestionListView(APIView):
    def get(self, request, pk=None):
        questions = Question.objects.all()
        ser_quest  = QuestionSerial(instance=questions, many=True)
        return Response(data=ser_quest.data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    def post(self, request, pk=None):
        ser_quest = QuestionSerial(data=request.data)
        if ser_quest.is_valid():
            ser_quest.save()
            return Response(ser_quest.data, status.HTTP_201_CREATED)
        return Response(ser_quest.errors, status.HTTP_400_BAD_REQUEST)
    

class QuestionUpdateView(APIView):
    def put(self, request, pk):
        question   = Question.objects.get(pk=pk)
        ser_quest = QuestionSerial(instance=question, data= request.data, partial=True)
        if ser_quest.is_valid():
            ser_quest.save()
            return Response(ser_quest.data, status.HTTP_200_OK)
        return Response(ser_quest.errors, status.HTTP_400_BAD_REQUEST)
    

class QuestionDeleteView(APIView):
    def delete(self, request, pk):
        qestion   = Question.objects.get(pk=pk)
        qestion.delete()
        return Response({'message':'question was deleted successfully'}, status.HTTP_200_OK)
            