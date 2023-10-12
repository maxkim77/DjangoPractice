from django.urls import path 
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notice/', views.notice, name='notice'),
    path('blog/', views.blog, name='blog'),
    path('blog/create/', views.blog_create, name='blog_create'),
    path('blog/update/<int:pk>/', views.blog_update, name='blog_update'),
    path('blog/delete/<int:pk>/', views.blog_delete, name='blog_delete'),
    path('accounts/signup/', views.signup, name='signup'),  # 실제 회원가입 뷰는 추가 구현 필요
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/profile/', views.profile, name='profile'), 
]
