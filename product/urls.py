from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.product_main, name='product_main'), # accounts/login
    path('product/<int:pk>/', views.product_contents, name='product_contents'), # accounts/logout
]