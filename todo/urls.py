from django.urls import path

from . import views

urlpatterns = [
    path('todos/', views.TodoAPIView.as_view(), name='api-todos'),
    path('todos/<int:pk>/', views.TodoAPIView.as_view(), name='api-todos-update')
]
