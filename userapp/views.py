from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Channel
from django.contrib.auth.models import User
from .serializers import ChannelSerializer, UserSerializer 

class ChannelListView(ListAPIView):  
    queryset = Channel.objects.all()  
    serializer_class = ChannelSerializer    
    filter_backends = [SearchFilter, ]  
    search_fields = ["name", ]
    permission_class = [IsAuthenticated, ]

class ChannelCreateView(CreateAPIView):  
    queryset = Channel.objects.all()  
    serializer_class = ChannelSerializer   

class ChannelGetView(RetrieveUpdateDestroyAPIView):  
    queryset = Channel.objects.all()  
    serializer_class = ChannelSerializer  
    permission_class = [IsAuthenticated, ]
    
class UserCreateView(CreateAPIView): 
    queryset = User.objects.all()  
    serializer_class = UserSerializer  
    
