from django import forms
from tinymce.widgets import TinyMCE
from .models import BlogPost

class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField(max_length=200)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 40,'rows': 20}))
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'content',
            'category',
            'cover_image',
            'tag',
        ]