from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(CustomUserSerializer, self).__init__(*args, **kwargs)
        if self.context and self.context['request'].method in ["PUT", "PATCH"]:
            self.fields.pop('email')
            self.fields.pop('password')

    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['email'] = instance.email
        return rep
