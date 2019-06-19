from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from adminback.models import MyUser, UserTicketModel
from goods.models import TypeInfo, GoodsInfo
from utils.functions import get_ticket


def register_back(request):
    if request.method == 'GET':
        return render(request, 'register_back.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        if not all([username, password, role]):
            msg = '参数不能为空'
            return render(request, 'register.html', {'msg': msg})
        # 对密码进行加密
        password = make_password(password)
        MyUser.objects.create(username=username, password=password, r_id=role)
        return HttpResponseRedirect(reverse('adminback:login_back'))


def login_back(request):
    if request.method == 'GET':
        return render(request, 'login_back.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if MyUser.objects.filter(username=username):
            user = MyUser.objects.get(username=username)
            if check_password(password, user.password):
                ticket = get_ticket()
                out_time = datetime.now() + timedelta(hours=1)
                res = HttpResponseRedirect(reverse('adminback:index_back'))
                res.set_cookie('ticket', ticket, expires=out_time)
                UserTicketModel.objects.create(user=user,
                                               ticket=ticket,
                                               out_time=out_time)
                return res
            else:
                msg = '密码错误'
                return render(request, 'login.html', {'msg': msg})
        else:
            msg = '用户不存在'
            return render(request, 'login.html', {'msg': msg})


def index_back(request):
    if request.method == 'GET':
        return render(request, 'index_back.html')


def productlist(request):
    if request.method == 'GET':
        num = request.GET.get('page_num', 1)  # 如果page_num有值就是page_num,没有就是1
        goods = GoodsInfo.objects.all()
        paginator = Paginator(goods, 3)  # 将商品信息分页，每页3条信息
        page = paginator.page(int(num))  # 拿到每一页的商品信息
        return render(request, 'product_list.html', {'page': page})

# 添加商品
def productdetail(request):
    if request.method == 'GET':
        types = TypeInfo.objects.all()
        return render(request,'product_detail.html', {'types': types})
    if request.method == 'POST':
        goodsname = request.POST.get('goodsname')
        goodsid = request.POST.get('goodsid')
        goodsprice = request.POST.get('goodsprice')
        goodspic = request.FILES.get('goodspic')
        goodsunit = request.POST.get('goodsunit')
        gkucun = request.POST.get('gkucun')
        gjianjie = request.POST.get('gjianjie')
        goodsclick = request.POST.get('goodsclick')
        gtype_id = request.POST.get('type')

        GoodsInfo.objects.create(goodsname=goodsname, goodsid=goodsid, goodsclick=goodsclick,
                                 goodsprice=goodsprice, goodspic=goodspic,
                                 goodsunit=goodsunit, gkucun=gkucun,
                                 gjianjie=gjianjie, gtype_id=gtype_id)
        return HttpResponseRedirect(reverse('adminback:productlist'))

# 删除商品
def productdel(request):
    if request.method == 'GET':
        g_id = request.GET.get('g_id')
        GoodsInfo.objects.filter(id=g_id).delete()
        return HttpResponseRedirect(reverse('adminback:productlist'))

# 编辑商品
def productedit(request):
    if request.method == 'GET':
        g_id = request.GET.get('g_id')
        goods = GoodsInfo.objects.filter(id=g_id).first()
        return render(request, 'product_edit.html', {'goods': goods})
    if request.method == 'POST':
        goodsid = request.POST.get('goodsid')
        goodspic = request.FILES.get('goodspic')
        goodsunit = request.POST.get('goodsunit')
        goodsclick = request.POST.get('goodsclick')
        goodsprice = request.POST.get('goodsprice')
        gkucun = request.POST.get('gkucun')
        gjianjie = request.POST.get('gjianjie')
        # get()查询的字段必须是主键或者唯一性约束的字段
        goods = GoodsInfo.objects.get(goodsid=goodsid)
        if goodspic:
            goods.goodspic = goodspic  # 如果图片有值就保存，如果没有值就不进行操作
        goods.goodsclick = goodsclick
        goods.goodsprice = goodsprice
        goods.gkucun = gkucun
        goods.goodsunit = goodsunit
        goods.gjianjie = gjianjie
        goods.save()
        return HttpResponseRedirect(reverse('adminback:productlist'))









