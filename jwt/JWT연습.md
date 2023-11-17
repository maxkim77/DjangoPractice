# Django 프로젝트 설정
새로운 Django 프로젝트를 생성

django-admin startproject project
cd 명령어를 사용하여 프로젝트 디렉토리로 이동합니다.
 
  
cd project
가상 환경을 생성하고 활성화합니다.
 
  
python -m venv venv
source venv/bin/activate  # Windows의 경우: venv\Scripts\activate
필요한 패키지를 설치합니다.
 
  
pip install django djangorestframework djangorestframework-simplejwt djoser django-cors-headers
requirements.txt 파일을 생성하고 위에서 설치한 패키지들을 추가합니다.
 
  
pip freeze > requirements.txt
Django 프로젝트의 설정 파일(settings.py)을 열어서 다음과 같이 설정합니다.

  
# project/settings.py

INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'corsheaders',
    'accounts',  # 나중에 생성할 앱 이름
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

MIDDLEWARE = [
    # ...
    'corsheaders.middleware.CorsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

AUTH_USER_MODEL = 'accounts.CustomUser'  # CustomUser 모델을 사용하도록 설정

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # 허용할 웹 애플리케이션 주소
]

SITE_ID = 1
데이터베이스를 마이그레이션합니다.
 
  
python manage.py migrate
accounts 앱을 생성하고 설정합니다.
 
  
python manage.py startapp accounts
accounts 앱의 모델과 관리자 계정을 생성하는 CustomUserManager 클래스를 managers.py 파일에 작성합니다.
  
# accounts/managers.py

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        if not username:
            raise ValueError(_('The Username field must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(username, email, password, **extra_fields)
CustomUser 모델을 models.py 파일에 작성합니다.

  
# accounts/models.py

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.crypto import get_random_string
from .managers import CustomUserManager

def generate_unique_username():
    return "user_" + get_random_string(8)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, default=generate_unique_username)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
accounts 앱의 시리얼라이저를 작성합니다.
  
# accounts/serializers.py

from dj_rest_auth.registration.serializers import RegisterSerializer as DefaultRegisterSerializer

class CustomRegisterSerializer(DefaultRegisterSerializer):
    # 필요한 경우 커스터마이즈한 내용을 추가
accounts 앱의 뷰를 작성합니다.

  
# accounts/views.py

from dj_rest_auth.registration.views import RegisterView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class CustomRegisterView(RegisterView):
    def get_response_data(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
URL 패턴을 설정합니다.

  
# accounts/urls.py

from django.urls import path, include
from .views import CustomRegisterView, mypage_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

urlpatterns = [
    path('join/', CustomRegisterView.as_view(), name='custom_register'),
    path('mypage/', mypage_view, name='mypage'),
]

# API 테스트를 위한 뷰
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mypage_view(request):
    return Response({"message": f"반갑습니다, {request.user.email}님!"})
프로젝트 루트의 urls.py 파일에 accounts 앱의 URL을 추가합니다.
  
# project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("account/", include("accounts.urls")),
]
Thunder Client를 사용한 API 테스트
Visual Studio Code(VSCode)에서 Thunder Client 확장 프로그램을 설치합니다.

VSCode의 왼쪽 사이드바에서 Thunder Client 아이콘을 클릭하여 Thunder Client를 엽니다.

Get 방식 선택후 mypage 주소 입력, 이후, Auth -> Bearer : {access token 입력}

Thunder Client는 요청을 실행하고 응답을 표시합니다. 이를 통해 API 엔드포인트를 테스트할 수 있습니다