from django.contrib import admin

# Register your models here.

from .models import Post, Like, FollowersCount

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(FollowersCount)
# This code registers the Post, Like, and FollowersCount models with the Django admin site.