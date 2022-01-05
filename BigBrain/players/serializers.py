from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.core import exceptions
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id',
                  'name',
                  'username',
                  'password',
                  'score',
                  ]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
                'required': True,
            },
            'id': {
                'read_only': True
            },
            'score': {
                'read_only': True
            },
            'username': {
                'required': True,
                'allow_blank': False
            },
            'name': {
                'required': True,
                'allow_blank': False
            },
        }

    def validate(self, data):
        passwordErrors = []
        errors = {}
        user = Player(**data)
        try:
            validate_password(data.get('password'), user)
        except exceptions.ValidationError as error:
            passwordErrors += list(error.messages)
        if passwordErrors:
            errors['Password'] = passwordErrors
        if errors:
            raise serializers.ValidationError(errors)
        return data

    def create(self, validated_data):
        user = Player(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
