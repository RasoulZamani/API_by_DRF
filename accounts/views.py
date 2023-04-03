from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerial, UserSerial
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

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
    

class UserViewSet(viewsets.ViewSet):
    permission_classes= [IsAuthenticated,]
    queryset = User.objects.all()
    
    def list(self, request):
        """list of all users"""
        ser_data = UserSerial(instance=self.queryset, many=True ).data
        return Response(data=ser_data)
    
    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        ser_data = UserSerial(instance=user).data
        return Response(data=ser_data)
    
    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        ser_data = UserSerial(instance=user, data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(data=ser_data.data)
        return Response(ser_data.errors)
    
    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        user.is_active =False
        return Response({'message':'user was deactivated!'})     
        