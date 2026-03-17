from .models import BaseRegistration,todolist
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


class PasswordCheange(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = BaseRegistration
        fields = ['password', 'confirm_password']

    def validate(self, attrs):
        password = attrs.get('password')
        pass2 = attrs.get('confirm_password')

        if password != pass2:
            raise serializers.ValidationError("Password not matched")

        return attrs

    def save(self, **kwargs):
        user = self.context.get('user')
        password = self.validated_data.get('password')

        user.set_password(password)
        user.save()   

class Todolist(serializers.Serializer):
    model=todolist
    fields='__all__'
    read_only_fields = ['user']

