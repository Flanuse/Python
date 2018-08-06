from django.core.paginator import Paginator
from django.shortcuts import render

from goods.models import TypeInfo, GoodsInfo


def index(request):
    if request.method == 'GET':
        typelist = TypeInfo.objects.all()
        goods1 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
        goods2 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
        goods3 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
        goods4 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
        goods5 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
        goods6 = typelist[5].goodsinfo_set.order_by('-id')[0:4]

        data = {
            'goods1': goods1,
            'goods2': goods2,
            'goods3': goods3,
            'goods4': goods4,
            'goods5': goods5,
            'goods6': goods6
        }

        return render(request, 'index.html', data)


def list(request, typeid, sort, pindex):
    if request.method == 'GET':
        typeinfo = TypeInfo.objects.get(id=int(typeid))
        # ?后面的参数可以通过request.GET.get('参数名')拿到
        if sort == '1':
            goodslist = GoodsInfo.objects.filter(gtype_id=int(typeid)).order_by('id')
        elif sort == '2':
            goodslist = GoodsInfo.objects.filter(gtype_id=int(typeid)).order_by('goodsprice')
        elif sort == '3':
            goodslist = GoodsInfo.objects.filter(gtype_id=int(typeid)).order_by('-goodsclick')
        paginator = Paginator(goodslist, 3)
        page = paginator.page(int(pindex))
        # 拿到最新的两个商品
        news = GoodsInfo.objects.filter(gtype_id=int(typeid)).order_by('-id')[0:2]

        data = {'news': news,
                'page': page,
                'typeinfo': typeinfo,
                'sort': sort}

        return render(request, 'list.html', data)


def detail(request, id):
    if request.method == 'GET':
        goods = GoodsInfo.objects.get(id=int(id))
        # goods.gtype 拿到该商品的type对象，再反查该type对应的商品
        news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
        data = {'goods': goods,
                'news': news}
        return render(request, 'detail.html', data)
