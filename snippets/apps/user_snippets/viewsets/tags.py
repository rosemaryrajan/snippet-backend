from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from apps.user_snippets.models import Tag
from apps.user_snippets.serializers.tag_detail import TagDetailSerializer
from apps.user_snippets.serializers.tags import TagSerializer


class TagViewSet(mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 GenericViewSet):
    model = Tag
    queryset = Tag.objects.all()
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        if self.action in ['list']:
            return TagSerializer

        elif self.action in ['retrieve']:
            return TagDetailSerializer
