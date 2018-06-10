from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
import hashlib
from django.http import HttpResponseRedirect, JsonResponse


# Create your views here.
def register(request):
    return render(request, 'register.html')


def register_handle(request):
    # 接受用户输入的请求 用户名，密码，确认密码，邮箱
    # 处理用户注册内容
    uname = request.POST.get('user_name', '无')
    upwd = request.POST.get('pwd', '无')
    upwd2 = request.POST.get('cpwd', '无')
    uemail = request.POST.get('email', '无')

    name_list = list(UserInfo.objects.all().values_list('uname'))
    email_list = list(UserInfo.objects.all().values_list('uemail'))
    if (uname,) not in name_list:
        if (uemail,) not in email_list:
            if upwd != upwd2:
                return redirect('/user/register/')
            s1 = hashlib.sha1()
            s1.update(upwd.encode('utf8'))
            upwd3 = s1.hexdigest()
            UserInfo.objects.create(uname=uname, upwd=upwd3, uemail=uemail)
            return redirect('/user/login')


def login(request):
    return render(request, 'login.html')


def login_handle(request):
    # 处理用户登录
    uname = request.POST.get('username', '没')
    pwd = request.POST.get('pwd', '没')
    s1 = hashlib.sha1()
    s1.update(pwd.encode('utf8'))
    pwd1 = s1.hexdigest()
    user = UserInfo.objects.all()
    for u in user:
        if u.uname == uname and u.upwd == pwd1:
            response = HttpResponseRedirect('/goods/index')

            response.set_cookie('username', uname, 3600)
            return response

    return redirect('/user/login')


def info(request):
    #个人信息
    name = request.COOKIES.get('username', '')
    context = UserInfo.objects.filter(uname=name)

    return render(request, 'user_center_info.html', {'name': name, 'context': context})


def order(request):
    #全部订单
    name = request.COOKIES.get('username', '')
    user = UserInfo.objects.get(uname=name)
    context = OrderInfo.objects.filter(user_id=user.id)
    a = []
    for i in context:
        list = UserCart.objects.filter(user_id=user.id).filter(isgo=1).filter(isshow=i.id)
        a.append(list)
    return render(request, 'user_center_order.html', {'name': name, 'context': context, 'list': a})


@csrf_exempt
def order_handle(request):
    #写入订单
    money = request.POST.get('key1')
    name = request.COOKIES.get('username', '')
    user = UserInfo.objects.get(uname=name)
    order = OrderInfo()
    order.user_id = user.id
    order.money = money
    list = UserCart.objects.filter(user_id=user.id).filter(isorder=1).filter(isgo=0)
    a = list.values_list('isbuy')
    if a[0][0] == True:
        order.isbuy = '已付款'
    order.array = 531698
    order.save()
    for i in list:
        if i != '' and i is not None:
            i.isgo = 1
            i.isshow = order.id
            i.save()

    return JsonResponse({'u': 'OK!'})


def site(request):
    #展示地址
    name = request.COOKIES.get('username', '')
    context = UserInfo.objects.filter(uname=name)
    return render(request, 'user_center_site.html', {'name': name, 'context': context})


def change_site(request):
    #修改地址
    name = request.COOKIES.get('username', '')
    user = UserInfo.objects.get(uname=name)
    user.ureceiveUser = request.POST.get('name', '')
    user.uaddress = request.POST.get('address', '')
    user.uzip_code = request.POST.get('code', '')
    user.uphone = request.POST.get('uphone', '')
    user.save()
    return render(request, 'user_center_site.html')
