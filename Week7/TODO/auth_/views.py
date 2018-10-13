from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('task_list')
        else:
            error = "login or password incorrect!!!"
            return render(request, 'login.html', {'error': error})
    else:
        return render(request, 'login.html')

def register(request):
    form = UserCreationForm(data = request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'login.html')
        else:
            error = "Your data is not appropriate!!!"
            return render(request, 'register.html', {'form': form, 'error': error})
    return render(request, 'register.html', {'form': form})

def logout(request):
    def logout(request):
        auth.logout(request)
    return redirect('login')


