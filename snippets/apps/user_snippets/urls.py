from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from apps.user_snippets import viewsets, views

snippet_api_router = DefaultRouter()
snippet_api_router.register(r'snippets', viewsets.SnippetViewSet, basename='snippets')
snippet_api_router.register(r'tags', viewsets.TagViewSet, basename='tags')
snippet_api_router.register(r'users', viewsets.UserViewSet, basename='users')

urlpatterns = snippet_api_router.urls + [
    path('auth/', obtain_auth_token, name='api_token_auth'),
    path('bulk-delete/', views.BulkSnippetDeleteView.as_view(), name='bulk-delete'),
    path('snippet-overview/', views.SnippetOverView.as_view(), name='snippet-overview'),
]
