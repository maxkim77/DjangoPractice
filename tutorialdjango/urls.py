from django.contrib import admin
from django.urls import path
from main.views import index, about, contact
from qna.views import qna_main, qna_contents
from product.views import  product_main, product_contents
from notice.views import notice, free_main, free_contents, oneone_main, oneone_contents

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # 이름 지정을 권장합니다.
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('qna/', qna_main, name='qna_main'),
    path('qna/<int:pk>/', qna_contents, name='qna_contents'),
    path('product/', product_main, name='product_main'),
    path('product/<int:pk>/', product_contents, name='product_contents'),
    path('notice/', notice, name='notice'),
    path('notice/free', free_main, name='free_main'),
    path('notice/free/<int:pk>/', free_contents, name='free_contents'),
    path('notice/oneone', oneone_main, name='oneone_main'),
    path('notice/onenone/<int:pk>/', oneone_contents, name='onenone_contents'),
]