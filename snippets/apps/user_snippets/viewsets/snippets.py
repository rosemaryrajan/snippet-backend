from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.user_snippets.models import Snippet
from apps.user_snippets.serializers.snippets import SnippetWriteSerializer, SnippetListSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    model = Snippet
    queryset = Snippet.objects.all()
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return SnippetWriteSerializer

        else:
            return SnippetListSerializer

    def create(self, request, *args, **kwargs):

        new_snippet = self.get_serializer_class()(data=request.data, context={'request': self.request})
        new_snippet.is_valid(raise_exception=True)
        snippet = new_snippet.save()

        return Response(
            SnippetListSerializer(instance=snippet, context={'request': self.request}).data,
            status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):

        partial = kwargs.pop('partial', False)
        snippet_data = self.get_serializer_class()(data=request.data, instance=self.get_object(),
                                                   partial=partial, context={'request': self.request})
        snippet_data.is_valid(raise_exception=True)
        snippet = snippet_data.save()
        return Response(
            SnippetListSerializer(instance=snippet, context={'request': self.request}).data)


