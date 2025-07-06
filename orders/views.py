from django.shortcuts import render
from django.http import JsonResponse


def ajax_cart(request):
    response = dict()
    response['message'] = 'Hello from server!'

    uid = request.GET['uid']
    pid = request.GET['pid']
    price = request.GET['price']

    response['uid'] = uid
    response['pid'] = pid
    response['price'] = price

    return JsonResponse(response)
