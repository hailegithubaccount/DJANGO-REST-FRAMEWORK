from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListCreateAPIView.as_view()),
    path('products/info/', views.ProductInfoAPIView.as_view()),
    path('products/<int:product_id>/', views.ProductDetailAPIView.as_view()),
    path('orders/', views.OrderListAPIView.as_view()),
    path('orders/<uuid:order_id>/', views.OrderDetailAPIView.as_view(), name='order-detail'),
    path('user-orders/', views.UserOrderListAPIView.as_view(), name='user-orders'),
    path('orders/create/', views.OrderCreateAPIView.as_view(), name='order-create'),
    path('orders/listOrders/', views.OrderListAPIView.as_view(), name='order-list'),
    path('register/', views.UserCreateAPIView.as_view(), name='user-register'),
    path('users/', views.UserListCreateAPIView.as_view(), name='user-list-create'),
]
