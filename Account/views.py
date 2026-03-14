from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .studentserializer import Studentlistserializer

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