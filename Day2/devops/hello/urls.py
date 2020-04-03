from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('userlist', views.list),          #列出所有用户
    path('addView', views.add_view),       #添加用户页面
    path('addsubmit', views.add_submit),   #添加用户后点提交动作的页面
    path('searchview', views.search_view), #查询用户页面
    path('search', views.search),          #查询用户后点提交动作的页面
    re_path('userupdate_view/([0-9]{1,5})', views.update_view),#更新用户操作的页面
    re_path('userupdate/([0-9]{1,5})', views.update),          #更新用户操作后点提交的页面
    re_path('userdelete/([0-9]{1,5})', views.delete),          #删除用户操作的页面
]