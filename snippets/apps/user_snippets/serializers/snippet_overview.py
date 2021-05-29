from rest_framework import serializers

from apps.user_snippets.serializers.snippets import SnippetListWithLinkSerializer


class SnippetOverViewSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    snippets = SnippetListWithLinkSerializer(many=True)
