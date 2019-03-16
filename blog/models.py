from django.conf import settings
from django.db import models
from django.utils import timezone





# модель для постов

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# модель для комментариев


class Comment(models.Model):
    author = models.CharField(max_length=10)
    text = models.CharField(max_length=100)
    post_pk = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text