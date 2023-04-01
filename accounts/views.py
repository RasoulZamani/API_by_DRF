from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerial

class UserRegisterView(APIView):
    def post(self, request):
        ser_user = UserRegisterSerial(data=request.POST)
        if ser_user.is_valid():
            User.objects.create_user( 
                username = ser_user.validated_data['username'],
                email    = ser_user.validated_data['email'],
                password = ser_user.validated_data['password'],
            )
            return Response(ser_user.validated_data)
        return Response(ser_user.errors)
        