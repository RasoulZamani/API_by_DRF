from rest_framework.views import APIView
from rest_framework.response import Response



class HomeView(APIView):
    def get(self, request):
        name = request.query_params['name']
        return Response({'greating':name})
    
    def post(self, request):
        name = request.data['name']
        return Response({'greating':name}) 