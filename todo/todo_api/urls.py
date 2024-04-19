from django.urls import path, include
from django.urls import re_path

from .views import (
    TodoListApiView,
    TodoDetailApiView,
)
from . import views


urlpatterns = [
    path('api', TodoListApiView.as_view()),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
    re_path('signup', views.signup),
    re_path('login', views.login),
    re_path('test_token', views.test_token),
]