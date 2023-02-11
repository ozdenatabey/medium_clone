from django import forms
from .models import BlogPost

class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField(max_length=200)
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'content',
            'category',
            'cover_image',
            'tag',
        ]