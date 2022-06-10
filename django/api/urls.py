from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('test',views.test,name='test'),
    path('post',views.post_new,name = 'post')
]