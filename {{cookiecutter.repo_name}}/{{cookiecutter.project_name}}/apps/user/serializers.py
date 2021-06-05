{% if cookiecutter.jwt == "y" or cookiecutter.jwt == "Y" %}
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
{% else %}
from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate
{% endif %}
from django.contrib.auth import get_user_model
from apps.utils.serializers import CustomUserSerializer

User = get_user_model()

{% if cookiecutter.jwt == "y" or cookiecutter.jwt == "Y" %}
class UserTokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['profile'] = ReadUserSerializer(self.user).data

        return data

class ReadUserSerializer(CustomUserSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']
{% else %}
class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)
    custom_error = {'error': 'Incorrect authentication credentials'}

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = authenticate(request=self.context.get('request'), username=email, password=password)
            if not user:
                raise exceptions.AuthenticationFailed({'password': self.custom_error['error']})
        else:
            raise exceptions.NotAuthenticated()
        attrs['user'] = user
        return attrs

{% endif %}

class UserSerializer(CustomUserSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
