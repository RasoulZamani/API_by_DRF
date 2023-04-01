from rest_framework import serializers
from django.contrib.auth.models import User


def clean_name(value):
    if 'fuck' in value:
        raise serializers.ValidationError('dont be rude!')
    return value

    
class UserRegisterSerial(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)
    class Meta:
        model = User
        fields = ('username','email', 'password','confirm_password')
        extra_kwargs = {
            'password': {'write_only':True},
            'username': {'validators':(clean_name,)},
        }
    # username = serializers.CharField(required=True)
    # email = serializers.EmailField(required=True)
    # password= serializers.CharField(required=True, write_only=True)
    # confirm_password = serializers.CharField(required=True, write_only=True)
    
    def validate_username(self, value):
        """ filed level validation for username field"""
        if value =='admin':
            raise serializers.ValidationError('username cant be admin')
        return value
    
    def validate(self, data):
        """obj level valiation for password confirmation"""
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('passwords should be equal')
        return data  