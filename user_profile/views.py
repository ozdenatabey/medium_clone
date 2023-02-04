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