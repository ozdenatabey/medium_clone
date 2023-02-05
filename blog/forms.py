from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    tag = forms.CharField(max_length=200)
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'category',
            'cover_image',
            'tag',
        ]