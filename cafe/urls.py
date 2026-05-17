from django.urls import path
from .views import *

urlpatterns=[
    path('', menu_view,name='menu'),
    path('add-to-cart/<int:variant_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
    path('increase/<str:key>/', increase_quantity, name='increase_quantity'),
    path('decrease/<str:key>/', decrease_quantity, name='decrease_quantity'),
    path('remove/<str:key>/', remove_item, name='remove_item'),
    path('place-order/', place_order, name='place_order'),
    path('order-success/', order_success, name='order_success'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('orders/', order_history, name='order_history'),
    path('payment-success/', payment_success, name='payment_success'),
]