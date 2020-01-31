from django.test import TestCase
from accounts.models import Status
from selenium.webdriver import Chrome



class StatusModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Status.objects.create(name='TestModel')

    def test_name_label(self):
        status = Status.objects.get(id=1)
        field_label = status._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Статус')

    def test_name_max_length(self):
        status = Status.objects.get(id=1)
        max_length = status._meta.get_field('name').max_length
        self.assertEquals(max_length, 500)

    def test_string_representation(self):
        status = Status(name="Test Name")
        self.assertEqual(str(status), status.name)

    def test_object_name_is_name(self):
        status = Status.objects.get(id=1)
        expected_object_name = '%s' % status.name
        self.assertEquals(expected_object_name, str(status))



class StatusViewTest(TestCase):
    def setUp(self):
        self.driver = Chrome()

    def tearDown(self):
        self.driver.close()

    def test_list_statuses(self):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.find_element_by_class_name('statuses').click()
        assert self.driver.current_url == 'http://127.0.0.1:8000/accounts/statuses/'

    def test_created_status(self):
        self.driver.get('http://localhost:8000/accounts/statuses/')
        self.driver.find_element_by_class_name('btn-outline-primary').click()
        self.driver.find_element_by_name('name').send_keys('Test')
        self.driver.find_element_by_class_name('btn-primary').click()
        assert self.driver.current_url == 'http://localhost:8000/accounts/statuses/'

    def test_updated_status(self):
        self.driver.get('http://127.0.0.1:8000/accounts/statuses/')
        self.driver.find_element_by_class_name('update').click()
        self.driver.find_element_by_name('name').clear()
        self.driver.find_element_by_name('name').send_keys('Test')
        self.driver.find_element_by_class_name('btn-primary').click()
        assert self.driver.current_url == 'http://127.0.0.1:8000/accounts/statuses/'

    def test_deleted_status(self):
        self.driver.get('http://127.0.0.1:8000/accounts/statuses/')
        self.driver.find_element_by_class_name('delete').click()
        self.driver.find_element_by_class_name('btn-danger').click()
        assert self.driver.current_url == 'http://127.0.0.1:8000/accounts/statuses/'