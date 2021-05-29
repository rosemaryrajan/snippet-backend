from django.contrib import admin

# Register your models here.
from apps.user_snippets.models.snippets import Snippet
from apps.user_snippets.models.tags import Tag

admin.site.register((Tag, Snippet), )
