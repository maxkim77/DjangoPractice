from django.urls import path
from .views import MainPageView, AboutPageView, ContactPageView, BlogListView, PostDetailView, BlogSearchView

urlpatterns = [
    path('', MainPageView.as_view(), name ='main'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('blog/search/', BlogSearchView.as_view(), name='blog_search')
]