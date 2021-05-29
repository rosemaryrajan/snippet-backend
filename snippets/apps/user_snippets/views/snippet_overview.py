from rest_framework import views
from rest_framework.permissions import IsAuthenticated

from apps.user_snippets.models import Snippet


class SnippetOverView(views.APIView):
    model = Snippet
    permission_classes = [IsAuthenticated, ]
