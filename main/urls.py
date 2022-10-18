from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('product-register',views.product_register,name='product_register'),
    path("dashboard/<str:pk>", views.dashboard, name="dashboard"),
    path("update/<str:pk>", views.updateItem, name="update"),
    path("delete/<str:pk>", views.deleteItem, name="delete"),
    path('login',views.login_user,name='login'),
    path('settings',views.acc_settings,name='settings'),
    path('logout',views.logout_user,name='logout'),
    path('sign-up',views.Signup,name='sign-up'),
    path('info/<str:pk>',views.info,name='info')
]
