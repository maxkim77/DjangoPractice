# memo_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.memo_list, name='memo_list'),
    # 다른 URL 패턴들도 추가할 수 있습니다.
]