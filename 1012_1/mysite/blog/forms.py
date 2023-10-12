# 이미지 추가
# forms.py
# fields = '__all__'로 하면 모든 필드 입력 가능
from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'contents', 'main_image'] # fields = '__all__'
