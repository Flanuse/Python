from django.conf.urls import url

from order import views

urlpatterns = [
    url(r'^order/', views.order, name='order'),
    # 返回订单页面
    # url(r'^order_info', views.order_info, name='order_info'),


]
