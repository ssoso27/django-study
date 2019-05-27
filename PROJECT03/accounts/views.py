from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import UserCustomChangeForm

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            user = form.save() # save 된 user를 받음
            auth_login(request, user) # request와 유저정보 넣기
            return redirect('boards:index') # 다른 app으로 redirect 가능
    else:
        form = UserCreationForm()
    return render(request, 'accounts/auth_form.html', {'form' : form})
    
def login(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) # 얘는 요청 관련 정보도 알아야함 -> request 도 넣어줌
        if form.is_valid() :
            # form.get_user : 입력된 user 정보 (id, pw 등)
            auth_login(request, form.get_user())
            return redirect('boards:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/auth_form.html', {'form': form})
        
    
def logout(request):
    if request.method=='POST':
        auth_logout(request)
        return redirect('boards:index')
    redirect('boards:index')
        
def delete(request):
    if request.method=='POST':
        request.user.delete()
    return redirect('boards:index')
    
def edit(request):
    if request.method=='POST':
        form = UserCustomChangeForm(request.POST, instance=request.user) # param1: 입력된 정보, params2: 기존 정보
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        form = UserCustomChangeForm(instance=request.user)
    return render(request, 'accounts/auth_form.html', {'form': form})
    
def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST) # param1: 요청 유저, param2: 입력된 정보
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('boards:index')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/auth_form.html', {'form' : form})