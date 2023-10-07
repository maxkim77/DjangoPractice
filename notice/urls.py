from django.urls import path
from . import views

urlpatterns = [
    path('notice/', views.notice, name='notice'),
    path('notice/free', views.free_main, name='free_mains'),
    path('notice/free/<int:pk>/', views.free_contents, name='free_contents'),
    path('notice/onenone', views.oneone_main, name='onenone_main'),  # 이름을 oneone_main으로 수정
    path('notice/onenone/<int:pk>/', views.oneone_contents, name='onenone_contents'),
]
