from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
from django.utils import timezone


def ajax_cart(request):
    response = dict()
    response['message'] = 'Hello from server!'

    uid = request.GET['uid']
    pid = request.GET['pid']
    price = request.GET['price']

    response['uid'] = uid
    response['pid'] = pid
    response['price'] = price

    # 1 - Створюємо нове замовлення та зберігаєм в БД:
    Order.objects.create(
        title=f'Order-{pid}/{uid}/{timezone.now()}',
        user_id=uid,
        product_id=pid,
        amount=float(price),
        notes='Очікує підтвердження'
    )

    # 2 - Зчитуємо із бази список всіх замовлень даного користувача:
    user_orders = Order.objects.filter(user_id=uid)

    # 3 -Обчислюємо загальну вартість всіх замовлень даного користувача:
    amount = 0
    for order in user_orders:
        amount += order.amount

    # 4 - Записуємо дані у відповідь сервера:
    response['amount'] = amount
    response['count'] = len(user_orders)

    # 5 - Відправляєм дані клієнту:
    return JsonResponse(response)

def index(request):
    return render(request, 'orders/index.html', context={
        'title': 'Управління кошиком',
        'page': 'index',
        'app': 'orders',
        'user_orders': Order.objects.filter(user_id=request.user.id)
    })