from django.conf.urls import url

from order import views

urlpatterns = [
    url(r'^order/', views.order, name='order'),
    # 返回订单页面
    # url(r'^order_info', views.order_info, name='order_info'),
    # 改变订单状态
    url(r'^orderchange/', views.orderchange, name='orderchange'),
    # 计算价格
    url(r'^amountprice/', views.amountprice, name='amountprice'),


]
