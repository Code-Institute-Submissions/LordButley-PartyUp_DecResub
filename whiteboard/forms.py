from .models import Post, Comment
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title' ,'content', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

# class EditForm(forms.ModelForm):
#     """ Edit a Post Form """
#     class Meta:
#         """
#         Get post model, choose fields to update and add summernote widget
#         """
#         model = Post
#         fields = (
#             'title', 'content',)
