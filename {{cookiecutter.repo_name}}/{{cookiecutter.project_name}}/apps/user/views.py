from django.contrib.auth import get_user_model
{% if cookiecutter.jwt == "y" or cookiecutter.jwt == "Y" %}
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.viewsets import ModelViewSet
{% else %}
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
{% endif %}
from rest_framework.response import Response
from rest_framework import status

from apps.user import serializers
from apps.utils.filters import CustomFilter

User = get_user_model()


class UserViewSet(ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    filter_backends = (CustomFilter,)
    custom_filter_fields = {"active": "is_active"}


{% if cookiecutter.jwt == "y" or cookiecutter.jwt == "Y" %}
class UserLoginAPIView(TokenViewBase):
    """
    post: Require Email And Password to Login.
    """

    serializer_class = serializers.UserTokenSerializer
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        profile = serializer.validated_data['profile']
        access = serializer.validated_data['access']
        refresh = serializer.validated_data['refresh']
        data = {'access': access, 'refresh': refresh, 'profile': profile}
        return Response(data, status=status.HTTP_200_OK)

{% else %}
class UserLoginAPIView(APIView):
    serializer_class = serializers.AuthTokenSerializer
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user = serializers.UserInformationSerializer(user).data
        data = {'token': token.key, 'user': user}
        return Response(data, status=status.HTTP_200_OK)
{% endif %}
