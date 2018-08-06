from django.conf.urls import url

from goods import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^list/(\d+)/(\d+)/(\d+)/', views.list, name='list'),
    url(r'^detail/(\d+)/', views.detail, name='detail'),

]
