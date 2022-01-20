from django.db import models
from django.conf import settings

class Video(models.Model): 
    name = models.CharField(max_length=50, blank=True)
    desc = models.CharField(max_length=300, blank=True)
    account = models.ForeignKey(settings.CHANNEL_MODEL, related_name="channel", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    video= models.URLField()
    likes = models.ManyToManyField(settings.CHANNEL_MODEL, related_name="video_likes", blank=True) 
    dislikes = models.ManyToManyField(settings.CHANNEL_MODEL, related_name="video_dislikes", blank=True) 

    class Meta:
        ordering = ["date"]

    def count_likes(self):
        if self.likes.count() > 0:
            return self.likes.count()
        else:
            return 0 

    def count_dislikes(self):
        if self.dislikes.count() > 0:
            return self.dislikes.count()
        else:
            return 0

    def str(self):
        return self.text

class Comment(models.Model):
    text = models.CharField(max_length=150) 
    video = models.ForeignKey(Video, related_name='post', on_delete=models.CASCADE)
    account = models.ForeignKey(settings.CHANNEL_MODEL, related_name="user_comments", on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.CHANNEL_MODEL, related_name="comment_likes",  blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def count_likes(self):
        if self.likes.count() > 0:
            return self.likes.count()
        else:
            return 0
    def __str__(self): 
        return self.text 

class Playlist(models.Model): 
    name = models.CharField(max_length=150) 
    channel =  models.ForeignKey(settings.CHANNEL_MODEL, related_name='posted', on_delete=models.SET_NULL, null=True, blank=True)
    video = models.ManyToManyField(Video)
    
    def __str__(self): 
        return self.name