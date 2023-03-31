from rest_framework import serializers

class PersonSerial(serializers.Serializer):
    name = serializers.CharField()
    age  = serializers.IntegerField()
    
    