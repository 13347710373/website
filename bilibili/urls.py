"""
created by lansen on
2020-06-09 17:44:30
"""
from django.urls import path
from .import views

app_name = 'bilibili'

urlpatterns = [
    path('run/', views.run_page, name='index'),
    #path('login/api/getuser/', views.getuser, name='getuser'),
    #path('login/api/postuser/', views.postuser, name='postuser')
]
