from .models import BaseRegistration
from rest_framework import serializers


class Studentlistserializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = BaseRegistration
        fields = [
            'username','first_name', 'last_name', 'email', 'password',
            'Address', 'gender','confirm_password'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Confirm Password Not Matched")
        return data
    
    def validate_email(self,value):
        if BaseRegistration.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is Already Exits")
        return value
    
    def validate_username(self,value):
        if BaseRegistration.objects.filter(username=value).exists():
            raise serializers.ValidationError("This Username is Already Exits")
        return value

    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['username'] = validated_data['email'] 
        user = BaseRegistration.objects.create_user(**validated_data)
        return user


class Loginserializer(serializers.ModelSerializer):
    username=serializers.CharField()
    password=serializers.CharField()

    class Meta:
     model=BaseRegistration
     fields=['username','password']


