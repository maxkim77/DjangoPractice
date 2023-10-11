# memo_app/views.py
from django.shortcuts import render
from .models import Memo

def memo_list(request):
    memos = Memo.objects.all()
    return render(request, 'memo_app/memo_list.html', {'memos': memos})

def memo_list(request):
    query = request.GET.get('q', '')
    
    if query:
        memos = Memo.objects.filter(title__icontains=query)
    else:
        memos = Memo.objects.all()
        
    return render(request, 'memo_app/memo_list.html', {'memos': memos})
