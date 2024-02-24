from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('osaindex',views.osaindex,name='osaindex'),
    path('first', views.first,name='first'),
    path('second', views.second,name='second'),
    path('third', views.third,name='third'),
    path('ee', views.ee,name='ee'),
    path('eein', views.eein,name='eein'),
    path('eenext', views.eenext,name='eenext'),
    path('eeenext', views.eeenext,name='eeenext'),
    path('osake', views.osake,name='osake'),
    path('osakein', views.osakein,name='osakein'),
    path('osaket', views.osaket,name='osaket'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('user', views.user, name='user'),
    path('new', views.new, name='new'),
    path('choice', views.choice, name='choice'),
    path('content/<int:num>', views.content, name='content'),
    path('post', views.post, name='post'),
    path('start/<int:num>', views.start, name='start'),
    path('startt/<int:num>', views.startt, name='startt'),
    path('starttt/<int:num>', views.starttt, name='starttt'),
    path('delete/<int:num>', views.delete, name='delete'),
    # path('favorite', views.favorite, name='favorite'),
    #path('gooddelete/<int:num>',views.gooddelete,name='gooddelete'),
    path('whogood', views.whogood, name='whogood'),
    path('deleteuser/<int:num>', views.deleteuser, name='deleteuser'),
    path('deletecontent/<int:num>', views.deletecontent, name='deletecontent'),
    path('add',views.add,name='add'),
    path('god/<int:odai_id>',views.god,name='god'),
    path('mypage',views.mypage,name='mypage'),
    path('mypage2',views.mypage2,name='mypage2'),
    path('followOdai/<int:num>',views.followOdai,name='followOdai'),

]