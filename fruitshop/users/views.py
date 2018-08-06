from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.models import UserModel, TicketModel
from utils.functions import get_ticket


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        if UserModel.objects.filter(username=username):
            user = UserModel.objects.get(username=username)
            if check_password(password, user.password):
                session_id = get_ticket()
                out_time = datetime.now() + timedelta(hours=1)
                res = HttpResponseRedirect(reverse('goods:index'))
                res.set_cookie('session_id', session_id, expires=out_time)
                # 将session_id保存到服务器上
                TicketModel.objects.create(user=user,
                                               session_id=session_id,
                                               out_time=out_time)
                return res
            else:
                msg = '密码错误'
                return render(request, 'login.html', {'msg': msg})
        else:
            msg = '用户不存在'
            return render(request, 'login.html', {'msg': msg})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        img = request.FILES.get('img')
        if not all([username, password, email]):
            msg = '参数不能为空'
            return render(request, 'register.html', {'msg': msg})
        # 对密码进行加密
        password = make_password(password)
        UserModel.objects.create(username=username,
                                 password=password,
                                 email=email, img=img)
        return HttpResponseRedirect(reverse('user:login'))


