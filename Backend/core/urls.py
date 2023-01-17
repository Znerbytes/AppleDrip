from django.urls import path
from .views import LogoutAPIView, PostsAPIView, RefreshAPIView, RegisterAPIView, LoginApiView, UserApiView

urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('login', LoginApiView.as_view()),
    path('user', UserApiView.as_view()),
    path('refresh', RefreshAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),
    path('insert_post', PostsAPIView.as_view()),
]
