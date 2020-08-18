from django import forms
from posts.models import Post

class CreatePostForm(forms.ModelForm):
    """Create post validation form based on Post model"""
    class Meta:
        """Form settings"""
        model = Post
        fields = ('user', 'profile', 'title', 'photo')