from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  url(r'^login/$', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
  url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
  url(r'^register/$', views.register, name='register'),
  url(r'^reset/$', auth_views.PasswordResetView.as_view(template_name='user/reset.html'), name='reset'),
]
