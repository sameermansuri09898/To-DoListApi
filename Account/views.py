from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from .studentserializer import Studentlistserializer,Loginserializer
from django.contrib.auth import authenticate,logout
from rest_framework.authtoken.models import Token

class StudentCreationsClass(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = Studentlistserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"msg": "Created Successfully",
             "user":serializer.data
             
             },
            status=status.HTTP_201_CREATED
        )
    
class LoginFunctionaluity(APIView):
    permission_classes=[AllowAny]
    def post(self,request,formate=None):
        serilizer=Loginserializer(data=request.data)
        serilizer.is_valid(raise_exception=True)

        username=serilizer.validated_data['username']
        password=serilizer.validated_data['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            token ,created =Token.objects.get_or_create(user=user)
            return Response({
                "mssg":"login sucesss",
                "token":token.key
            })
      
          
class LogoutUser(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        request.user.auth_token.delete()

        return Response({
            "message": "Logout successful"
        })