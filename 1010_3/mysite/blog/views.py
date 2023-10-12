# blog > views.py
from django.shortcuts import render

# mooc db
db = [
    {
        'id': 1,
        'title': '과제 1',
        'contents': '과제 2',
        'created_at': '2023-10-10 00:00:00',
        'updated_at': '2023-10-11 00:00:00',
        'author': '머니언',
        'category': '일상',
        'tags': '체력단련, 무예단련',
        'thumbnail': 'https://picsum.photos/200/300',
    },
    {
        'id': 2,
        'title': '과제2',
        'contents': '과제2',
        'created_at': '2023-10-12 00:00:00',
        'updated_at': '2023-10-13 00:00:00',
        'author': '머니언',
        'category': '테크',
        'tags': '맥북, 아이폰, 파이썬',
        'thumbnail': 'https://picsum.photos/200/300',
    },
    {
        'id': 3,
        'title': '과제 3',
        'contents': '과제 3',
        'created_at': '2023-10-14 00:00:00',
        'updated_at': '2023-10-15 00:00:00',
        'author': '세종대왕',
        'category': '취미',
        'tags': '그림, 서예',
        'thumbnail': 'https://picsum.photos/200/300',
    },
]

def blog(request):
    # db = Blog.objects.all()
    context = {
        'db': db,
    }
    return render(request, 'blog/blog.html', context)

def post(request, pk):
    # db = Blog.objects.get(pk=pk)
    context = {
        'db': db[pk-1],
    }
    return render(request, 'blog/post.html', context)