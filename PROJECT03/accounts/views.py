from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            user = form.save() # save 된 user를 받음
            auth_login(request, user) # request와 유저정보 넣기
            return redirect('boards:index') # 다른 app으로 redirect 가능
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form' : form})
    
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) # 얘는 요청 관련 정보도 알아야함 -> request 도 넣어줌
        if form.is_valid() :
            # form.get_user : 입력된 user 정보 (id, pw 등)
            auth_login(request, form.get_user())
            return redirect('boards:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
        
    
def logout(request):
    if request.method=='POST':
        auth_logout(request)
        return redirect('boards:index')
    redirect('boards:index')
        