import random
import string

import factory
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase, Client, RequestFactory, LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver

from todos.models import Todo
from todos.views import TodoList


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: "Agent %03d" % n)
    email = factory.LazyAttributeSequence(lambda o, n: f'{o.username}{n}@example.com')
    password = factory.PostGenerationMethodCall('set_password')


class TodoFactory(factory.DjangoModelFactory):
    class Meta:
        model = Todo

    user = factory.SubFactory(UserFactory, password=random_string_generator())
    title = 'MyTitle'
    text = 'MyText'


class TodoTests(TestCase):
    def test_str(self):
        todo = TodoFactory()
        self.assertEqual(str(todo), 'MyTitle')


class TodoListViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_no_todos_in_context(self):
        request = self.factory.get('/')
        request.user = UserFactory(password=random_string_generator())
        response = TodoList.as_view()(request)
        self.assertEquals(list(response.context_data['latest']), [],)

    def test_todos_in_context(self):
        request = self.factory.get('/')
        todo = TodoFactory()
        request.user = todo.user
        response = TodoList.as_view()(request)
        self.assertEquals(list(response.context_data['latest']), [todo],)


class CreatePostIntegrationTest(LiveServerTestCase):
    selenium = None

    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        cls.password = random_string_generator()
        cls.user = UserFactory(password=cls.password)
        cls.client = Client()
        super(CreatePostIntegrationTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(CreatePostIntegrationTest, cls).tearDownClass()

    def test_create_todo(self):
        self.assertTrue(self.client.login(username=self.user.username, password=self.password))
        cookie = self.client.cookies[settings.SESSION_COOKIE_NAME]
        # Replace `localhost` to 127.0.0.1 due to the WinError 10054 according to the
        # https://stackoverflow.com/a/14491845/1360307
        self.selenium.get(f'{self.live_server_url}{reverse("todos:create")}'.replace('localhost', '127.0.0.1'))
        if cookie:
            self.selenium.add_cookie({
                'name': settings.SESSION_COOKIE_NAME,
                'value': cookie.value,
                'secure': False,
                'path': '/'})
        self.selenium.refresh()  # need to update page for logged in user
        self.selenium.find_element_by_id('id_title').send_keys('MyTitle')
        self.selenium.find_element_by_id('id_text').send_keys('MyText')
        self.selenium.find_element_by_xpath('//input[@type="submit"]').click()
        self.assertEqual(Todo.objects.first().title, 'MyTitle')
