from rest_framework import serializers
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Work, Artist

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
             'username')


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
            'username', 'email', 'password')
        read_only_fields = ['id']
        extra_kwargs = {'password':{'write_only': True, 'min_length':4}}

    def create(self, validated_data):
        user = User.objects.create_user(
        validated_data['username'],
        validated_data['email'])

        user.set_password(validated_data['password'])
        user.save()
        return user


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = (
            'link', 'work_type')


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = (
            'name', 'work')
