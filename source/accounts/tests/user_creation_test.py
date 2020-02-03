from django.test import TestCase
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome


class LoginTest(TestCase):
    def setUp(self):
        self.driver = Chrome()

    def tearDown(self):
        self.driver.close()

    def test_create_user(self):
        self.driver.get('http://127.0.0.1:8000/accounts/user_create')
        self.driver.find_element_by_name('username').send_keys('student6')
        self.driver.find_element_by_name('password').send_keys('test')
        self.driver.find_element_by_name('password_confirm').send_keys('test')
        self.driver.find_element_by_name('first_name').send_keys('Иван')
        self.driver.find_element_by_name('last_name').send_keys('Иванов')
        self.driver.find_element_by_name('email').send_keys('student6@mail.ru')
        self.driver.find_element_by_name('citizenship').send_keys('Гаваи')
        self.driver.find_element_by_name('series').send_keys('Ф123456789')
        self.driver.find_element_by_name('issued_by').send_keys('ГК РФ')
        self.driver.find_element_by_name('issued_date').send_keys('03/19/2019')
        self.driver.find_element_by_name('address').send_keys('Hawaii')
        self.driver.find_element_by_name('inn').send_keys('Hawaii12345')
        self.driver.find_element_by_name('nationality').send_keys('Гаваец')
        self.driver.find_element_by_name('sex').send_keys('женский')
        self.driver.find_element_by_name('birth_date').send_keys('03/19/2019')
        self.driver.find_element_by_name('patronymic').send_keys('Иванович')
        self.driver.find_element_by_name('phone_number').send_keys('+996700998877')
        self.driver.find_element_by_name('address_fact').send_keys('Марсианин')
        self.driver.find_element_by_name('role').send_keys('student')
        self.driver.find_element_by_name('status').send_keys('Очная форма обучения')
        self.driver.find_element_by_name('social_status').send_keys('Сирота')
        self.driver.find_element_by_name('admin_position').send_keys('Студент')
        self.driver.find_element_by_css_selector('input[type="submit"]').click()
        self.driver.get('http://127.0.0.1:8000/accounts/6/')
        try:
            link = self.driver.find_element_by_link_text("Главная")
        except NoSuchElementException:
            link = None
        assert link is not None

    def test_login_error(self):
        self.driver.get('http://127.0.0.1:8000/accounts/login/')
        self.driver.find_element_by_name('username').send_keys('adminanet')
        self.driver.find_element_by_name('password').send_keys('adminanet')
        self.driver.find_element_by_css_selector('button[type="submit"]').click()
        assert self.driver.current_url.split('?')[0] == 'http://127.0.0.1:8000/accounts/login/'
        error = self.driver.find_element_by_css_selector('.text-danger')
        assert error.text == "Неверное имя пользователя или пароль."


class LogoutTest(TestCase):
    def setUp(self):
        self.driver = Chrome()

    def tearDown(self):
        self.driver.close()

    def test_logout_as_admin(self):
        self.driver.get('http://127.0.0.1:8000/accounts/login/')
        self.driver.find_element_by_name('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_css_selector('button[type="submit"]').click()
        self.driver.find_element_by_class_name('logout').click()
        assert self.driver.current_url == 'http://127.0.0.1:8000/'

