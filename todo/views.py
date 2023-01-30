from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from . import serializers
from .models import Todo


# Create your views here.
class TodoAPIView(ListCreateAPIView, UpdateModelMixin, DestroyModelMixin):
    queryset = Todo.objects.all()
    serializer_class = serializers.TodoSerializer

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
