from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAuthenticated
from .studentserializer import Studentlistserializer,Loginserializer,PasswordChangeSerializer,Todolist
from django.contrib.auth import authenticate,logout
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from .models import todolist

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
        return Response({
            "mssg":"Password Does not Matched"
        })
      
          
class LogoutUser(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        request.user.auth_token.delete()

        return Response({
            "message": "Logout successful"
        })

class Changepasswordclass(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PasswordChangeSerializer(
            data=request.data,
            context={'request': request}
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Password updated successfully"
        }) 


class TodoClass(viewsets.ViewSet):

    permission_classes=[IsAuthenticated]

    def list(self,request,pk=None):
        userlogin=todolist.objects.filter(user=request.user)
        serializer=Todolist(userlogin,many=True)
        return Response(serializer.data)
    
    def create(self,request,formate=None):
        serializer=Todolist(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self,request,pk=None):
        try:
            todoes=todolist.objects.get(pk=pk , user=request.user)
        except todolist.DoesNotExist:
            return Response({"mssg":"Usr not Found"})
        serializer=Todolist(todoes)
        return Response(serializer.data)
    
    def update(self,request,pk=None):
# eee
        try:
            todoes=todolist.objects.get(pk=pk,user=request.user)
        except todolist.DoesNotExist:
            return Response({"mssg":"user not Found"})
        
        serializer=Todolist(todoes,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def partial_update(self,request,pk=None):

        try:
            todoes=todolist.objects.get(pk=pk,user=request.user)
        except todolist.DoesNotExist:
            return Response({"mssg":"user not Found"})
        
        serializer=Todolist(todoes ,data=request.data ,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()    

    def destroy(self,request,pk=None):
        try:
            todoes=todolist.objects.get(pk=pk , user=request.user)

        except todolist.DoesNotExist:
            return Response({"Not found"})
        todoes.delete()
        return Response({"mssg":"delete Successfully"})


          
