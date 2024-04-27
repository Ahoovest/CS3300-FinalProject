from django.test import TestCase, Client
from django.urls import reverse
from workout_app.models import User, Plan, Workout
from .forms import PlanForm, WorkoutForm, RegistrationForm
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from django.test import LiveServerTestCase
from selenium.webdriver import Firefox

# Create your tests here.
class MyModelTestCase(TestCase):
  
    def setUp(self):
        self.user = User.objects.create(username='test_user', email='test@example.com')
        self.plan = Plan.objects.create(title='Test Plan', is_active=True, about='Test Plan Description')
        self.workout = Workout.objects.create(title='Test Workout', description='Test Workout Description', plan=self.plan)

    def test_user_str(self):
        self.assertEqual(str(self.user), 'test_user')

    def test_plan_str(self):
        self.assertEqual(str(self.plan), 'Test Plan')

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Test Workout')

class FormTestCase(TestCase):
    def test_plan_form_valid_data(self):
        form = PlanForm(data={'title': 'Test Plan', 'about': 'Test Description', 'is_active': True})
        self.assertTrue(form.is_valid())

    def test_workout_form_valid_data(self):
        form = WorkoutForm(data={'title': 'Test Workout', 'description': 'Test Description'})
        self.assertTrue(form.is_valid())

    def test_plan_form_invalid_data(self):
        # Test invalid data for PlanForm
        form = PlanForm(data={})  # Empty data
        self.assertFalse(form.is_valid())

    def test_workout_form_invalid_data(self):
        # Test invalid data for WorkoutForm
        form = WorkoutForm(data={})  # Empty data
        self.assertFalse(form.is_valid())

class ViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
        self.plan = Plan.objects.create(title='Test Plan', is_active=True, about='Test Description')
        self.workout = Workout.objects.create(title='Test Workout', description='Test Description', plan=self.plan)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workout_app/index.html')

    def test_plan_list_view(self):
        response = self.client.get(reverse('plan_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workout_app/plan_list.html')

    def test_plan_detail_view(self):
        response = self.client.get(reverse('plan_detail', args=[self.plan.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workout_app/plan_detail.html')

    def test_add_plan_view_authenticated(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('add_plan'), {'title': 'New Plan', 'about': 'New Description', 'is_active': True})
        self.assertEqual(response.status_code, 302)  # Redirects after successful form submission
        self.assertTrue(Plan.objects.filter(title='New Plan').exists())

    def test_add_plan_view_unauthenticated(self):
        response = self.client.get(reverse('add_plan'))
        self.assertEqual(response.status_code, 302)  # Redirects to login page
        self.assertIn('/accounts/login/', response.url)

    # Add more test methods for other views similarly

    def test_user_register_view(self):
        response = self.client.get(reverse('user_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workout_app/register.html')

    def test_user_login_view(self):
        response = self.client.get(reverse('user_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workout_app/login.html')

    def test_user_logout_view(self):
        response = self.client.get(reverse('user_logout'))
        self.assertEqual(response.status_code, 302)  # Redirects after logout

class SeleniumUserRegistrationTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_user_registration(self):
        self.browser.get(self.live_server_url + '/user/register/')
        username_input = self.browser.find_element_by_name('username')
        username_input.send_keys('testuser')
        email_input = self.browser.find_element_by_name('email')
        email_input.send_keys('test@example.com')
        password1_input = self.browser.find_element_by_name('password1')
        password1_input.send_keys('password123')
        password2_input = self.browser.find_element_by_name('password2')
        password2_input.send_keys('password123')
        submit_button = self.browser.find_element_by_xpath('//button[@type="submit"]')
        submit_button.click()
        self.assertIn('index', self.browser.current_url)

class SeleniumUserLoginTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_user_login(self):
        self.browser.get(self.live_server_url + '/user/login/')
        username_input = self.browser.find_element_by_name('username')
        username_input.send_keys('testuser')
        password_input = self.browser.find_element_by_name('password')
        password_input.send_keys('password123')
        submit_button = self.browser.find_element_by_xpath('//button[@type="submit"]')
        submit_button.click()
        self.assertIn('index', self.browser.current_url)

class SeleniumPlanCreationTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_plan_creation(self):
        self.browser.get(self.live_server_url + '/add/plan/')
        title_input = self.browser.find_element_by_name('title')
        title_input.send_keys('Test Plan')
        about_input = self.browser.find_element_by_name('about')
        about_input.send_keys('Test Description')
        is_active_checkbox = self.browser.find_element_by_name('is_active')
        is_active_checkbox.click()
        submit_button = self.browser.find_element_by_xpath('//button[@type="submit"]')
        submit_button.click()
        self.assertIn('index', self.browser.current_url)

class SeleniumPlanDetailTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_plan_detail(self):
        # Assuming there's a plan with ID 1 in the database
        self.browser.get(self.live_server_url + '/plan/1/')
        # Add assertions here to verify the details of the plan displayed on the page
        # For example:
        plan_title = self.browser.find_element_by_xpath('//h1').text
        self.assertEqual(plan_title, 'Test Plan')

class SeleniumLogoutTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_user_logout(self):
        self.browser.get(self.live_server_url + '/user/logout/')
        # Assuming it redirects to the login page upon successful logout
        self.assertIn('login', self.browser.current_url)