from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .utils import send_verification_email, check_verification_token


def signup(request):
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

        # 3 - Формуємо негативний звіт:
        if user is None:
            color = 'red'
            message = 'Не вдалось зберегти дані користувача в базі'
        
        else:
            # 4 - Робота із E-mail:
            user.is_active = False  # Деактивуємо користувача до підтвердження email
            user.save()
            send_verification_email(request, user)

            # - 5 - Формуємо позитивний звіт:
            color = 'green'
            message = 'Будь ласка, перевірте свою електронну пошту для підтвердження реєстрації'

        # 6 - Завантаження сторінки звіту:
        return render(request, 'accounts/report.html', context={
            'title': 'Звіт про реєстрацію',
            'page': 'report',
            'app': 'accounts',
            'color': color,
            'message': message
        }) 


def signin(request):
    if request.method == 'GET':
        return render(request, 'accounts/signin.html', context={
            'title': 'Авторизація',
            'page': 'signin',
            'app': 'accounts'
        })
    elif request.method == 'POST':
        # 1 - Отримуємо дані із форми:
        login_x = request.POST.get('username')
        pass1_x = request.POST.get('pass1')

        # 2 - Перевіряємо чи є такий користувач в БД:
        user = authenticate(request, username=login_x, password=pass1_x)

        # 3 - Користувач знайдений та активний:
        if user is not None:
            login(request, user)
            color = 'green'
            message = 'Авторизація успішно!'
        
        # 4 - Користувач не знайдений або неактивний:
        else:
            try:
                potential_user = User.objects.get(username=login_x)
            except User.DoesNotExist:
                potential_user = None
            
            # 5 - Користувач знайдений, але неактивний:
            if potential_user is not None and not potential_user.is_active:
                color = 'red'
                message = 'Ваш акаунт не активований!'

            # 6 - Користувач не знайдений:
            else:
                color = 'red'
                message = 'Користувач не знайдений'

        # 7 - Завантаження сторінки звіту:
        return render(request, 'accounts/report.html', context={
            'title': 'Звіт про авторизацію',
            'page': 'report',
            'app': 'accounts',
            'color': color,
            'message': message
        }) 


def signout(request):
    logout(request)
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
    login_y = request.GET.get('username')
    # ->
    try:
        User.objects.get(username=login_y)
        response['message'] = 'Логін - зайнятий!'
    except User.DoesNotExist:
        response['message'] = 'Логін - вільний!'
    # ->
    return JsonResponse(response)

def activate(request, uidb64, token):
    """ 
    Activate user account after email verification.
    """
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # ->
    if user is not None and check_verification_token(user, token):
        user.is_active = True
        user.save()
        message = 'Ваш акаунт успішно активовано!'
        color = 'green'
    else:
        message = 'Посилання для активації недійсне'
        color = 'red'

    # ->
    return render(request, 'accounts/report.html', context={
            'title': 'Звіт про активацію',
            'page': 'report',
            'app': 'accounts',
            'color': color,
            'message': message
        }) 