from email import message
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse


from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context: dict[str, str] = {
        'title': 'Sweet Point - Авторизация',
        'form': form
    }

    return render(request, 'users/login.html', context)

@login_required # чтобы не было доступа и перенапр на логин
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, " Ваши данные успешно обновлены")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context: dict[str, str] = {
        'title': 'Sweet Point - Профиль',
        'form': form
    }

    return render(request, 'users/profile.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
        
    context: dict[str, str] = {
        'title': 'Sweet Point - Регистрация',
        'form': form
    }

    return render(request, 'users/registration.html', context)

@login_required
def logout(request):
    messages.success(request, "Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))
