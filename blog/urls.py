'''
Created on Jul 19, 2015

@author: zhengxu
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]   
