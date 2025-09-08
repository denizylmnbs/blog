from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User 
from .serializers import UserSerializer

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset =  User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  

class MeView(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)