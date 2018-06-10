from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.core.paginator import *
from UserApp.models import *


# Create your views here.
def index(request):
    #展示首页
    context = TypeInfo.objects.all()
    a = TypeInfo.objects.all().values_list('id')
    str = []
    for b in a:
        for i in b:
            result = GoodsInfo.objects.all().filter(gtype_id=i)[0:4]
            for q in result:
                str.append(q)
    name = request.COOKIES.get('username', '')
    return render(request, 'index.html', {'context': context, 'str': str, 'name': name})


def list(request, type_id, pindex):
    #列表
    context = GoodsInfo.objects.filter(gtype_id=type_id)
    if pindex == '':
        pindex = 1
    paginator = Paginator(context, 2)
    page = paginator.page(int(pindex))
    name = request.COOKIES.get('username', '')
    return render(request, 'list.html', {'pag': page, 'id': type_id, 'name': name})


def deatil(request, good_id):
    #详情页
    context = GoodsInfo.objects.filter(id=good_id)
    name = request.COOKIES.get('username', '')
    return render(request, 'detail.html', {'context': context, 'name': name})


def cart(request):
    #展示购物车
    name = request.COOKIES.get('username', '')
    user = UserInfo.objects.get(uname=name)
    cart = UserCart.objects.filter(user_id=user.id).filter(isdelete=0).filter(isorder=0)
    list1 = []
    for car in cart:
        list1.append(car)
    a = len(list1)
    return render(request, 'cart.html', {'name': name, 'count': list1, 'a': a})


@csrf_exempt
def join_cart(request):
    #加入购物车
    name = request.COOKIES.get('username', '')
    id = request.POST.get('key2')
    count = request.POST.get('key1')
    user = UserInfo.objects.get(uname=name)
    if UserCart.objects.filter(good_id=int(id)).filter(isorder=0) is True:
        cart = UserCart.objects.get(good_id=int(id))
        cart.count = int(count) + cart.count
        cart.save()
    else:
        print('hh')
        UserCart.objects.create(user_id=user.id, good_id=int(id), count=int(count))
    return JsonResponse({'u': '添加成功'})


@csrf_exempt
def delete_cart(request):
    #删除购物车
    id = request.POST.get('key1')
    car = UserCart.objects.get(id=id)
    car.isdelete = 1
    car.save()
    return JsonResponse({'u': ' 删除成功 '})



@csrf_exempt
def order(request):
    #处理购物车
    name = request.COOKIES.get('username', '')
    user = UserInfo.objects.get(uname=name)
    id = request.POST.get('key1')
    count = request.POST.get('key2')
    money = request.POST.get('key3')
    if id != '' and count != '':
        if id is not None and count is not None:
            cart = UserCart.objects.get(id=int(id))
            cart.count = int(count)
            cart.money = money
            cart.isorder = 1
            cart.save()
            return JsonResponse({'u': 'OK!'})
    cart = UserCart.objects.filter(user_id=user.id).filter(isdelete=0).filter(isorder=1).filter(isgo=0)
    a = len(cart)
    me = cart.values_list('money')
    list = []
    for i in me:
        for b in i:
            list.append(float(b))
    my = sum(list)
    q = round(my, 2)
    z = q + 10
    return render(request, 'place_order.html', {'name': name, 'car': cart, 'a': a, 'my': q, 'me': z})
