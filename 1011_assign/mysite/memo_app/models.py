# memo_app/models.py
from django.db import models

class Memo(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='memos/')
    content = models.TextField()

    def __str__(self):
        return f"{self.date} - {self.title}"
