from django.test import TestCase
from todos.models import Todo


class TodoTests(TestCase):
    def test_str(self):
        t = Todo(title='MyTodo', text='MyText')
        self.assertEqual(str(t), 'MyTodo')
