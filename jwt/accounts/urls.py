# accounts/urls.py
from django.contrib import admin
from .views import mypage_view  # 'mypage_view' 함수를 import합니다.
from django.urls import path, include
from .views import mypage_view, CustomRegisterView

urlpatterns = [
    path('join/', CustomRegisterView.as_view(), name='custom_register'),
    path("", include("dj_rest_auth.urls")),
    path('mypage/', mypage_view, name='mypage'),
]
