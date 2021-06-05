from django.urls import path

from rest_framework.routers import DefaultRouter

from user import views

router = DefaultRouter()

router.register('user', views.UserViewSet, basename='user_viewset')

urlpatterns = [
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
]

urlpatterns += router.urls
