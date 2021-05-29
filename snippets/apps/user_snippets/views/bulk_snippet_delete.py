from drf_yasg.utils import swagger_auto_schema
from rest_framework import views
from rest_framework.response import Response

from apps.user_snippets.models import Snippet
from apps.user_snippets.serializers.snippets import SnippetDEleteSerializer, SnippetListSerializer


class BulkSnippetDeleteView(views.APIView):
    @swagger_auto_schema(request_body=SnippetDEleteSerializer)
    def post(self, request, *args, **kwargs):
        snippet_list = SnippetDEleteSerializer(data=request.data, context={'request': self.request})
        snippet_list.is_valid(raise_exception=True)
        Snippet.objects.filter(id__in=snippet_list.validated_data['snippet_list']).delete()
        snippets = Snippet.objects.all()
        return Response(
            SnippetListSerializer(instance=snippets, context={'request': self.request}, many=True).data)
