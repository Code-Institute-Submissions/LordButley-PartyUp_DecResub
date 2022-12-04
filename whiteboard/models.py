""" Models for the PARTY UP app.
Models consist of tables for Games, Posts and Comments """

from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):

    """Model for games"""

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    banner = models.ImageField()
    ref_name = models.CharField(max_length=200)

    class Meta:

        """Class to order model by id"""

        ordering = ['id']

    def __str__(self):
        return str(self.title)


class Post(models.Model):

    """Model for posts"""

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="whiteboard_posts")
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    most_recent = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        """Class to order model by id"""

        ordering = ['-most_recent']

    def __str__(self):
        return str(self.title)


class Comment(models.Model):

    """Model for posts"""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="whiteboard_comments")
    name = models.CharField(max_length=80)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:

        """Class to order model by creation time"""

        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.content} by {self.name}"
