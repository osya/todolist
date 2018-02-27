import random
import string

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase, RequestFactory, TestCase
from django.urls import reverse

import chromedriver_binary
import factory
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options

from todos.models import Todo
from todos.views import TodoList


def random_string_generator(size=10,
                            chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# pragma pylint: disable=R0903
class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: 'Agent %03d' % n)
    email = factory.LazyAttributeSequence(
        lambda o, n: f'{o.username}{n}@example.com')
    password = factory.PostGenerationMethodCall('set_password')


class TodoFactory(factory.DjangoModelFactory):
    class Meta:
        model = Todo

    user = factory.SubFactory(UserFactory, password=random_string_generator())
    title = 'raw title'
    text = 'raw text'


# pragma pylint: enable=R0903


class TodoTests(TestCase):
    def test_todo_create(self):
        todo = TodoFactory()
        self.assertEqual(1, Todo.objects.count())
        self.assertEqual('raw title', todo.title)


class TodoListViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_no_todos_in_context(self):
        request = self.factory.get('/')
        request.user = UserFactory(password=random_string_generator())
        response = TodoList.as_view()(request)
        self.assertEqual(
            list(response.context_data['latest']),
            [],
        )

    def test_todos_in_context(self):
        request = self.factory.get('/')
        todo = TodoFactory()
        request.user = todo.user
        response = TodoList.as_view()(request)
        self.assertEqual(
            list(response.context_data['latest']),
            [todo],
        )


class CreatePostIntegrationTest(LiveServerTestCase):
    selenium = None

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--log-level=3')
        cls.selenium = webdriver.WebDriver(
            executable_path=chromedriver_binary.chromedriver_filename,
            chrome_options=chrome_options)
        cls.password = random_string_generator()
        super(CreatePostIntegrationTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(CreatePostIntegrationTest, cls).tearDownClass()

    def setUp(self):
        # `user` creation placed in setUp() rather than setUpClass(). Because when `user` created in setUpClass then
        # `test_todo_create` passed when executed separately, but failed when executed in batch
        # TODO: investigate this magic
        self.user = UserFactory(password=self.password)

    def test_todo_list(self):
        response = self.client.get(reverse('todos:list'))
        self.assertIn(response.status_code, (301, 302))

    def test_slash(self):
        response = self.client.get(reverse('home'))
        self.assertIn(response.status_code, (301, 302))

    def test_empty_create(self):
        response = self.client.get(reverse('todos:create'))
        self.assertIn(response.status_code, (301, 302))

    def test_todo_create(self):
        self.assertTrue(
            self.client.login(
                username=self.user.username, password=self.password))
        cookie = self.client.cookies[settings.SESSION_COOKIE_NAME]
        # Replace `localhost` to 127.0.0.1 due to the WinError 10054 according to the
        # https://stackoverflow.com/a/14491845/1360307
        self.selenium.get(
            f'{self.live_server_url}{reverse("todos:create")}'.replace(
                'localhost', '127.0.0.1'))
        if cookie:
            self.selenium.add_cookie({
                'name': settings.SESSION_COOKIE_NAME,
                'value': cookie.value,
                'secure': False,
                'path': '/'
            })
        self.selenium.refresh()  # need to update page for logged in user
        self.selenium.find_element_by_id('id_title').send_keys('raw title')
        self.selenium.find_element_by_id('id_text').send_keys('raw text')
        self.selenium.find_element_by_xpath(
            '//*[@id="submit-id-create"]').click()
        self.assertEqual(1, Todo.objects.count())
        self.assertEqual('raw title', Todo.objects.first().title)
