from django.test import TestCase

from accounts.models import AdminPosition
from selenium.webdriver import Chrome


class AdminPositionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        AdminPosition.objects.create(name='TestModel')

    def test_object_is_object(self):
        position = AdminPosition.objects.get(id=1)
        self.assertEquals(position.name, 'TestModel')

    def test_verbose_name(self):
        position = AdminPosition.objects.get(id=1)
        field_label = position._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название')

    def test_verbose_name_plural(self):
        self.assertEqual(str(AdminPosition._meta.verbose_name_plural), "Должности")

    def test_max_length(self):
        position = AdminPosition.objects.get(id=1)
        max_length = position._meta.get_field('name').max_length
        self.assertEquals(max_length, 500)

    def test_string_representation(self):
        position = AdminPosition.objects.get(id=1)
        self.assertEqual(str(position.name), position.name)


class AdminPositionViewTest(TestCase):
    def setUp(self):
        self.driver = Chrome()

    def tearDown(self):
        self.driver.close()

    def test_list_position(self):
        self.driver.get('http://localhost:8000/accounts/adminpositions/')
        self.driver.find_element_by_name('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_css_selector('button[type="submit"]').click()
        assert self.driver.current_url == 'http://localhost:8000/accounts/adminpositions/'

    def test_created_position(self):
        self.driver.get('http://localhost:8000/accounts/adminpositions/')
        self.driver.find_element_by_name('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_css_selector('button[type="submit"]').click()
        self.driver.find_element_by_class_name('btn-success').click()
        self.driver.find_element_by_name('name').send_keys('CreateTest')
        try:
            self.driver.find_element_by_class_name('btn-success').click()
            assert self.driver.current_url == 'http://localhost:8000/accounts/adminpositions/'
        except:
            assert self.driver.find_element_by_tag_name('h3')

    def test_updated_position(self):
        self.driver.get('http://localhost:8000/accounts/adminpositions/')
        self.driver.find_element_by_name('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_css_selector('button[type="submit"]').click()
        self.driver.find_element_by_class_name('update').click()
        self.driver.find_element_by_name('name').clear()
        self.driver.find_element_by_name('name').send_keys('UpdateTest')
        try:
            self.driver.find_element_by_class_name('btn-primary').click()
            assert self.driver.current_url == 'http://localhost:8000/accounts/adminpositions/'
        except:
            assert self.driver.find_element_by_tag_name('h3')


    def test_deleted_position(self):
        self.driver.get('http://localhost:8000/accounts/adminpositions/')
        self.driver.find_element_by_name('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_css_selector('button[type="submit"]').click()
        self.driver.find_element_by_class_name('delete').click()
        self.driver.find_element_by_class_name('btn-danger').click()
        assert self.driver.current_url == 'http://localhost:8000/accounts/adminpositions/'
