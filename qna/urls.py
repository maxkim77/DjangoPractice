from django.urls import path
from . import views

urlpatterns = [
    path('qna/', views.qna_main, name='qna_main'), # accounts/login
    path('qna/<int:pk>/', views.qna_contents, name='qna_contents'), # accounts/logout
]