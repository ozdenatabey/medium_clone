from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import json

from .forms import BlogPostModelForm
from .models import Category, Tag, BlogPost

@login_required(login_url='user:login_view')
def create_blog_post_view(request):
    form = BlogPostModelForm()
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            print(form.cleaned_data)
            f.user = request.user
            f.save()
            tags = json.loads(form.cleaned_data.get('tag'))
            for item in tags:
                tag_item, created = Tag.objects.get_or_create(title=item.get('value').lower())
                tag_item.is_active = True
                tag_item.save()
                f.tag.add(tag_item)
            messages.success(request,'Blog Postunuz Başarıyla Oluşturuldu. Ana Sayfaya Yönlendiriliyorsunuz..')
            return redirect('home_view')
            
    context = dict(
        form=form
    )
    return render(request, 'blog/create_blog_post.html', context)
