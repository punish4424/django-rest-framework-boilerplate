from django.urls import path

from user import views

urlpatterns = [
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
]
