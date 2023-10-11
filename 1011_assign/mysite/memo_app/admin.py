# memo_app/admin.py
from django.contrib import admin
from .models import Memo

@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'content',)
