from rest_framework.serializers import ModelSerializer 
from .models import Channel
from django.contrib.auth.models import User

class ChannelSerializer(ModelSerializer): 
    class Meta: 
        model = Channel 
        fields = "__all__" 

class UserSerializer: 
    class Meta: 
        model = User 
        fields = "__all__" 