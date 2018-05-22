from django.shortcuts import render, redirect,reverse
from django.contrib import auth
from django.http import HttpResponseRedirect

# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    if request.method == 'POST':
        username = request.POST.get('username', )
        password = request.POST.get('password', )

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render('index.html', {'message': '登录ok'})
        else:
            return HttpResponseRedirect('error', {'message': '登录失败'})


def register(request):
    return render(request, 'user/register.html')

def loginout(request):
    auth.logout(request)
    return render(request, 'index.html')
