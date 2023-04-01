from rest_framework import serializers

class UserRegisterSerial(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password= serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)
    def validate_usrname(self, value):
        """ filed level validation for username field"""
        if value =='admin':
            raise serializers.ValidationError('username cant be admin')
        return value
    
    def validate(self, data):
        """obj level valiation for password confirmation"""
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('passwords should be equal')
        return data  