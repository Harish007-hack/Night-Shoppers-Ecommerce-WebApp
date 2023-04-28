from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('product-register',views.product_register,name='product_register'),
    path("dashboard/<str:pk>", views.dashboard, name="dashboard"),
    path("update/<str:pk>", views.updateItem, name="update"),
    path("delete/<str:pk>", views.deleteItem, name="delete"),
    path("delete-order/<str:pk>", views.deleteOrder, name="deleteOrder"),
    path('login',views.login_user,name='login'),
    path('settings',views.acc_settings,name='settings'),
    path('logout',views.logout_user,name='logout'),
    path('sign-up',views.Signup,name='sign-up'),
    path('info/<str:pk>',views.Cart_order,name='info'),
    path('status/<str:pk>',views.status_update,name='status_update'),
    path('reset_password',auth_views.PasswordResetView.as_view(template_name="main/resetpass.html"),name='reset_password'),
    path('reset_password_done',auth_views.PasswordResetDoneView.as_view(template_name="main/resetdone.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="main/reset.html"),name='password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name="main/resetcomplete.html"),name='password_reset_complete'),
    path('payment',views.payment,name='payment'),
    path('order-summary',views.summary,name='order-summary'),
    path('cart-update/<str:pk>/<str:action>/',views.update_cart,name='update-cart'),
    path('cart-delete-item/<str:pk>',views.delete_cart_item,name='cart-delete-item'),
    path('checkout',views.checkout,name='checkout'),
    # path('add-coupon',views.addCoupon,name='add-coupon'),

]
