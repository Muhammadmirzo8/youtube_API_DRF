from django.db import models

from django.contrib.auth.models import User
from django.db import models

from django.conf import settings


class Channel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150, blank=True)
    profile_pic = models.URLField(blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subscribes = models.ManyToManyField(settings.CHANNEL_MODEL, related_name="channel_subscribes", blank=True, symmetrical=False)
    subscribers = models.ManyToManyField(settings.CHANNEL_MODEL, related_name="channel_subscribers", blank=True, symmetrical=False)

    def count_followers(self):
        if self.followers.count() > 0:
            return self.followers.count()
        else:
            return 0

    def show_channels(self):
        return self.subscribes

    def __str__(self):
        return self.user.username
