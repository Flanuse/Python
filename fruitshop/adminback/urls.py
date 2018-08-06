from django.conf.urls import url

from adminback import views

urlpatterns = [
    url(r'^login_back/', views.login_back, name='login_back'),
    url(r'^register_back/', views.register_back, name='register_back'),
    # 后台主页
    url(r'^index_back/', views.index_back, name='index_back'),
    # 商品列表
    url(r'^productlist/', views.productlist, name='productlist'),
    # 商品详情
    url(r'^productdetail/', views.productdetail, name='productdetail'),
    # 删除商品
    url(r'^productdel', views.productdel, name='productdel'),
    # 编辑商品
    url(r'^productedit', views.productedit, name='productedit'),



]
