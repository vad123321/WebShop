from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
from django.utils import timezone
from catalog.models import Product
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


def ajax_cart(request):
    response = dict()
    response['message'] = 'Hello from server!'

    uid = request.GET['uid']
    pid = request.GET['pid']
    price = request.GET['price']

    response['uid'] = uid
    response['pid'] = pid
    response['price'] = price

    order = Order.objects.filter(user_id=uid, product_id=pid, notes='Очікує підтвердження').first()
    if order:
        order.quantity += 1
        order.save()
    else:
        Order.objects.create(
            title=f'Order-{pid}/{uid}/{timezone.now()}',
            user_id=uid,
            product_id=pid,
            amount=float(price),
            notes='Очікує підтвердження',
            quantity=1
        )

    # 1 - Створюємо нове замовлення та зберігаєм в БД:
    # Order.objects.create(
    #     title=f'Order-{pid}/{uid}/{timezone.now()}',
    #     user_id=uid,
    #     product_id=pid,
    #     amount=float(price),
    #     notes='Очікує підтвердження',
    #     quantity=1
    # )

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


def ajax_cart_indicate(request):
    response = dict()
    uid = request.GET['uid']
    user_orders = Order.objects.filter(user_id=uid)
    # ->
    amount = 0
    for order in user_orders:
        amount += order.amount
    # ->
    response['amount'] = amount
    response['count'] = len(user_orders)
    return JsonResponse(response)


def index(request):
    return render(request, 'orders/index.html', context={
        'title': 'Управління кошиком',
        'page': 'index',
        'app': 'orders',
        'user_orders': Order.objects.filter(user_id=request.user.id)
    })


def bill(request, sel_list: str):
    # ->
    sel_list_str = sel_list.split(',')
    sel_list_num = [int(x) for x in sel_list_str[:-1]]
    total_price = int(sel_list_str[-1])
    final_list = []
    # ->
    for order_id in sel_list_num:
        order = Order.objects.get(id=order_id)
        final_list.append({
            'product_name': order.product.name,
            'category_name': order.product.category.name,
            'product_price': order.product.price,
            'product_photo': order.product.photo
        })
    # ->
    return render(request, 'orders/bill.html', context={
        'title': 'Сторінка замовлення',
        'page': 'bill',
        'app': 'orders',
        'total_price': total_price,
        'final_list': final_list,
        'init_list': sel_list
    })


def confirm(request, init_list: str):
    if request.method == 'GET':
        return render(request, 'orders/confirm.html', context={
            'title': 'Підтвердження замовлення',
            'page': 'confirm',
            'app': 'orders',
            'init_list': init_list,
        })
    elif request.method == 'POST':
        pass


@csrf_exempt
def delete_order(request):
    if request.method == 'POST':
        order_id = request.POST.get('id')
        try:
            Order.objects.get(id=order_id).delete()
            return JsonResponse({'success': True})
        except Order.DoesNotExist:
            return JsonResponse({'success': False})
    return JsonResponse({'success': False})
