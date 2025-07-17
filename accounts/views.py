from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def signup(request):
    response = dict()
    if request.method == 'GET':
        return render(request, 'accounts/signup.html', context={
            'title': 'Реєстрація',
            'page': 'signup',
            'app': 'accounts'
        })
    elif request.method == 'POST':
        # 1 - Отримуємо дані із форми:
        login_x = request.POST.get('username')
        pass1_x = request.POST.get('pass1')
        pass2_x = request.POST.get('pass2')
        email_x = request.POST.get('email')

        # 2 - Додаємо користувача в базу:
        user = User.objects.create_user(login_x, email_x, pass1_x)

        # 3 - Формуємо звіт:
        if user is None:
            response['color'] = 'red'
            response['message'] = 'Не вдалось зберегти дані користувача в базі'
        else:
            user.save()
            response['color'] = 'green'
            response['message'] = 'Реєстрація успішно завершена!'

        return render(request, 'accounts/report.html', context={
            'title': 'Звіт про реєстрацію',
            'page': 'report',
            'app': 'accounts',
            'response': response
        }) 


def signin(request):
    response = dict()
    if request.method == 'GET':
        return render(request, 'accounts/signin.html', context={
            'title': 'Авторизація',
            'page': 'signin',
            'app': 'accounts'
        })
    elif request.method == 'POST':
        # data handling ...

        return render(request, 'accounts/report.html', context={
            'title': 'Звіт про авторизацію',
            'page': 'report',
            'app': 'accounts',
            'response': response
        })


def signout(request):
    # ...
    return render(request, 'accounts/signout.html', context={
        'title': 'Вихів',
        'page': 'signout',
        'app': 'accounts'
    })


def profile(request):
    # ...
    return render(request, 'accounts/profile.html', context={
        'title': 'Профіль',
        'page': 'profile',
        'app': 'accounts'
    })


def ajaxreg(request):
    response = dict()
    response['message'] ='AJAX -> OK'
    # ...
    return JsonResponse(response)