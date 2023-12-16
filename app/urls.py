from django.urls import include, path
from . import views

urlpatterns = [
    # path('master',views.Master,name='master'),    
    path('',views.Index,name='home'),

    path('signup',views.signup,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    # cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    # contact page
    path("contact", views.contact_page, name="contact"),

    # checkout Page
    path("cart/cart-detail/checkout",views.checkout, name="checkout"),
    # Order Page
    path("order",views.user_order, name="order"),
    #Product page
    path("product/", views.product,name="product"),
    path("product/<str:id>", views.product_detail,name="product_detail"),
    # serach mehtod
    path('search',views.search,name='search')
]
