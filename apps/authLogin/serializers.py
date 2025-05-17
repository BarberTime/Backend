from rest_framework import serializers
from .models import AuthLogin   

class AuthLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthLogin
        fields = '__all__'  