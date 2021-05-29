from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.user_snippets.models import Snippet
from apps.user_snippets.serializers.snippet_overview import SnippetOverViewSerializer


class SnippetOverView(views.APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, *args, **kwargs):
        snippets = Snippet.objects.all()
        response_dict = {'count': snippets.count(),
                         'snippets': snippets}
        return Response(SnippetOverViewSerializer(instance=response_dict, context={'request': self.request}).data)
