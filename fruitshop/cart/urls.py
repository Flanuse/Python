from django.conf.urls import url

from cart import views

urlpatterns = [
    url(r'^addtocart/', views.addtocart, name='addtocart'),
    url(r'^subtocart/', views.subtocart, name='subtocart'),
    # 刷新页面
    url(r'^goodsnum/', views.goodsnum, name='goodsnum'),
    # 加入购物车
    url(r'^tocart/', views.tocart, name='tocart'),
    # 总价
    url(r'^totalprice/', views.totalprice, name='totalprice'),
    # 删除购物车中的商品
    url(r'^deletegoods/', views.deletegoods, name='deletegoods'),
    # 改变购物车中商品的状态
    url(r'^changestatus/', views.changestatus, name='changestatus')


]
