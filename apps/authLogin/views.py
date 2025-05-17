from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AuthLogin
from .serializers import AuthLoginSerializer  

class AuthLoginView(APIView):
    def post(self, request):
        serializer = AuthLoginSerializer(data=request.data)
        if serializer.is_valid():
            auth_login = serializer.save()      
            return Response({'message': 'AuthLogin creado exitosamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            