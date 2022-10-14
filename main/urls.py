from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path("dashboard", views.dashboard, name="dashboard"),
    path('login',views.login_user,name='login'),
    path('settings',views.acc_settings,name='settings'),
    path('logout',views.logout_user,name='logout'),
    path('sign-up',views.Signup,name='sign-up'),
    path('info',views.info,name='info')
]
