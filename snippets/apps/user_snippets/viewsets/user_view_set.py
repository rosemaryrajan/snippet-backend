from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import status, mixins
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.user_snippets.serializers.user_serializer import UserSerializer, UserReadSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):
    model = settings.AUTH_USER_MODEL
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return UserSerializer
        else:
            return UserReadSerializer

    def create(self, request, *args, **kwargs):

        new_user = self.get_serializer_class()(data=request.data,
                                               context={'request': self.request})
        new_user.is_valid(raise_exception=True)
        user = new_user.save()
        return Response(
            UserReadSerializer(instance=user, context={'request': self.request}).data,
            status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object():
            partial = kwargs.pop('partial', False)
            updated_user = self.get_serializer_class()(data=request.data, instance=self.get_object(),
                                                       partial=partial, context={'request': self.request})
            updated_user.is_valid(raise_exception=True)
            user = updated_user.save()
            return Response(
                UserReadSerializer(instance=user, context={'request': self.request}).data)
        else:
            raise PermissionDenied
