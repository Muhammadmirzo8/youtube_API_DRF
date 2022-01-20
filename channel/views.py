from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter 
from rest_framework.permissions import IsAuthenticated

from .models import Video, Comment, Playlist
from .serializers import VideoSerializer, PlaylistSerializer, CommentSerializer



class VideoListCreateView(ListCreateAPIView):  
    queryset = Video.objects.all()  
    serializer_class = VideoSerializer   
    permission_class = [IsAuthenticated, ] 
    filter_backends = [SearchFilter, ]  
    search_fields = ["name", ]

class VideoGetView(RetrieveUpdateDestroyAPIView):  
    queryset = Video.objects.all()  
    serializer_class = VideoSerializer  
    permission_class = [IsAuthenticated, ]  

class PlaylistListCreateView(ListCreateAPIView):  
    queryset = Playlist.objects.all()  
    serializer_class = PlaylistSerializer   
    permission_class = [IsAuthenticated, ] 
    filter_backends = [SearchFilter, ]  
    search_fields = ["name", ]

class PlaylistGetView(RetrieveUpdateDestroyAPIView):  
    queryset = Playlist.objects.all()  
    serializer_class = PlaylistSerializer  
    permission_class = [IsAuthenticated, ]  

class CommentListCreateView(ListCreateAPIView):  
    queryset = Comment.objects.all()  
    serializer_class = CommentSerializer   
    permission_class = [IsAuthenticated, ] 
    filter_backends = [SearchFilter, ]  
    search_fields = ["name", ]

class CommentGetView(RetrieveUpdateDestroyAPIView):  
    queryset = Comment.objects.all()  
    serializer_class = CommentSerializer  
    permission_class = [IsAuthenticated, ] 




