from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework import serializers


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'password', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if self.instance is not None:

            if 'username' in data and data['username']:
                raise serializers.ValidationError('email cannot be edited')
            if 'password' in data and data['password']:
                raise serializers.ValidationError('Use change password api for password change')
        return data

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = super().create(validated_data)
        return user

    def update(self, instance, validated_data):

        if 'password' in validated_data and validated_data['password']:
            validated_data['password'] = make_password(validated_data['password'])
        user = super().update(instance, validated_data)
        return user
