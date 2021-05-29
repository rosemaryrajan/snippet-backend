from django.conf import settings
from django.db import models


class Snippet(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='get_snippets', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    snippet = models.TextField()
    tags = models.ManyToManyField('user_snippets.Tag', related_name='get_snippet', blank=True)

    def __str__(self):
        return self.title
