from rest_framework import serializers

from apps.user_snippets.models import Snippet, Tag
from apps.user_snippets.serializers.tags import TagSerializer


class SnippetDEleteSerializer(serializers.Serializer):
    snippet_list = serializers.ListField(child=serializers.IntegerField())


class SnippetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'snippet', 'tags', 'created_on')

    tags = TagSerializer(many=True)


class SnippetWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('title', 'snippet', 'tags_list')

    tags_list = serializers.ListField(child=serializers.CharField(max_length=50), allow_null=True, required=False)

    def get_tags(self, validated_data):
        tag_list = []
        for item in validated_data['tags_list']:
            try:
                tag = Tag.objects.get(title=item)
                tag_list.append(tag.id)
            except Tag.DoesNotExist:
                tag = Tag.objects.create(title=item)
                tag_list.append(tag.id)
        return tag_list

    def create(self, validated_data):
        # validated_data['user'] = self.context['request'].user
        tag_list = []
        if 'tags_list' in validated_data:
            tag_list = self.get_tags(validated_data)
            validated_data.pop('tags_list')
        snippet = super().create(validated_data)
        if tag_list:
            for tag_list_item in tag_list:
                snippet.tags.add(tag_list_item)
        return snippet

    def update(self, instance, validated_data):

        tag_list = []
        if 'tags_list' in validated_data:
            tag_list = self.get_tags()
            validated_data.pop('tags_list')
        snippet = super().update(instance, validated_data)
        if tag_list:
            snippet.tags.add(tag_list)
        return snippet
