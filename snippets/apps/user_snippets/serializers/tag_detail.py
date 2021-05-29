from rest_framework import serializers

from apps.user_snippets.models import Tag
from apps.user_snippets.serializers.snippets import SnippetListSerializer


class TagDetailSerializer(serializers.ModelSerializer):
    #
    class Meta:
        model = Tag
        fields = ('id', 'title', 'snippets')

    snippets = SnippetListSerializer(source='get_snippet', many=True)
