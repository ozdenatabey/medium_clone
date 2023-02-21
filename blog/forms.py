from django import forms
from django.core import validators
from tinymce.widgets import TinyMCE
from .models import BlogPost

# Our Validations
from config.denetimler import min_lenght_3

class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField(max_length=200)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 40,'rows': 20}))
    # title = forms.CharField(validators=[validators.MinLengthValidator(3, message="En az 3 karakter girmelisin..")])
    title = forms.CharField(validators=[min_lenght_3,])

    class Meta:
        model = BlogPost
        fields = [
            'title',
            'content',
            'category',
            'cover_image',
            'tag',
        ]

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if len(title) < 3:
    #         raise forms.ValidationError('Title bilgisi en az 3 karakterden oluşmalıdır..')
    #     return title.upper()