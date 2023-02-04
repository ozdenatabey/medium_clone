from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    # login olan kullanici direk olarak ana sayfaya gitsin
    if request.user.is_authenticated:
        messages.info(request, f'{request.user.username}Daha önce login olmuşsun.')
        return redirect('home_view')

    context = dict()
    if request.method == "POST":
        # print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if len(username) < 6 or len(password) < 6:
            messages.warning(request, f'Lutfen Bilgileri Dogru Giriniz..')
            return redirect('user_profile:login_view')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'{request.user.username}Login oldun.')
            # login oldugunu kullaniciya belli edelim
            return redirect('home_view')
    return render(request, 'user_profile/login.html', context)

def logout_view(request):
    messages.info(request, f'{request.user.username}Oturum kapatildi.')
    logout(request)
    return redirect('home_view')

def register_view(request):
    context = dict()
    if request.method == "POST":
        post_info = request.POST
        email = post_info.get('email')
        email_confirm = post_info.get('email_confirm')
        first_name = post_info.get('first_name')
        last_name = post_info.get('last_name')
        password = post_info.get('password')
        password_confirm = post_info.get('password_confirm')
        instagram = post_info.get('instagram')
        print('*'*30)
        print(email, email_confirm, password, password_confirm, first_name, last_name, instagram)
        print('*'*30)
    return render(request, 'user_profile/register.html', context)