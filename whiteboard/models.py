from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    banner = models.ImageField()
    ref_name = models.CharField(max_length=200)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="whiteboard_posts")
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    most_recent = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-most_recent']

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=80)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.content} by {self.name}"

