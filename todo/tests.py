from django.shortcuts import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

import todo.models as models
import todo.views as views


# Create your tests here.
class TestTodo(APITestCase):
    def test_list_returns_all_todos(self):
        todos = [
            models.Todo.objects.create(title=f"Title {i + 1}", description=f"description {i + 1}", done=False)
            for i in range(5)
        ]

        response = self.client.get(reverse('api-todos'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(todos))

    def test_create_valid_todo_passes(self):
        todo = {
            'title':       'Title Test',
            'description': 'This is a long description about a todo and what should be done',
        }

        response = self.client.post(reverse('api-todos'), data=todo, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Todo.objects.count(), 1)

    def test_toggle_todo_state_passes(self):
        todo = models.Todo.objects.create(title="Title", description="desc", done=False)

        factory = APIRequestFactory()
        request = factory.patch(reverse('api-todos-update', kwargs={'pk': todo.pk}), data={'done': 'true'})
        view = views.TodoAPIView.as_view()
        response = view(request, pk=todo.pk)
        todo = models.Todo.objects.get()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(todo.done)
