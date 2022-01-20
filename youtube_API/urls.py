"""youtube_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from userapp.views import ChannelListView,ChannelCreateView,ChannelGetView , UserCreateView 
from channel.views import VideoListCreateView, VideoGetView, PlaylistListCreateView, PlaylistGetView, CommentListCreateView, CommentGetView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi 
from rest_framework.permissions import AllowAny

doc_view = get_schema_view(
        openapi.Info(
            title="Clone API of Youtube", 
            default_version = 'v1', 
            descrption = '(REST API) Clone API of Youtube using Dajngo Rest Framework', 
            contact = openapi.Contact("Muhammadmirzo Toshpolatjonov <mtoshpulatjonov@gmail.com>")
        ), 
        public=True, 
        permission_classes=(AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('get/token/',TokenObtainPairView.as_view()), 
    path('refresh/token/',TokenRefreshView.as_view()),  
    #docs
    path("", doc_view.with_ui('swagger', cache_timeout=0), name="swagger_doc") , 
    path("redoc/", doc_view.with_ui('redoc', cache_timeout=0), name="redoc_doc"),
    #userapp 
    path('user/create/', UserCreateView.as_view(), name='user-create'),
    path('Channel/',ChannelListView.as_view(), name='accounts-list'), 
    path('Channel/create/', ChannelCreateView.as_view(), name='accounts-create'), 
    path('Channel/<int:pk>/', ChannelGetView.as_view(), name='account-get'), 
    #channel 
    path("video/", VideoListCreateView.as_view(), name="video-list-create"),
    path('video/<int:pk>', VideoGetView.as_view(), name="video-get"),
    path("playlist/", PlaylistListCreateView.as_view(), name="playlist-list-create"),
    path('playlist/<int:pk>', PlaylistGetView.as_view(), name="playlist-get"), 
    path("comment/", CommentListCreateView.as_view(), name="comment-list-create"), 
    path('comment/<int:pk>', CommentGetView.as_view(), name="comment-get")

]
