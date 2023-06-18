from django.test import TestCase
from django.urls import reverse_lazy, reverse

from apps.accounts.models import CustomUser


class UserAuthenticationTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.email = 'test@test.pl'
        self.user = CustomUser.objects.create_user(username=self.username, password=self.password, email=self.email)

    def test_login(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Log out')

    def test_logout(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Log in')

    def test_failed_login(self):
        response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'wrongpassword'},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter a correct username and password.')

    # def test_access_protected_view(self):
    #     response = self.client.get('/protected-view/')
    #     self.assertEqual(response.status_code,
    #                      302)  # Assuming unauthenticated access to protected view redirects to login page
    #
    #     # You can check if the login page is returned in the response
    #     self.assertTemplateUsed(response, 'login.html')
