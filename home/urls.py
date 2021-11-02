from django.contrib import admin
from django.urls import path
from home import views
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', views.homepage),
    path('signup', views.handlesignup),
    path('login', views.handlelogin),
    path('logout', views.handlelogout),
    path('submitqs', views.handleqssubmit),
    path('like', views.handlelike),
    path('question', views.handlequestion),
    path('answering', views.handleanswering),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]