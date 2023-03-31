from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerial

class HomeView(APIView):
    def get(self, request):
        #name = request.query_params['name']
        persons = Person.objects.all()
        serial_pers = PersonSerial(instance=persons, many=True)
        return Response(data=serial_pers.data)

    
    def post(self, request):
        name = request.data['name']
        return Response({'greating':name}) 