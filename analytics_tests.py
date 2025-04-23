from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

class AnalyticsTestCase(TestCase)
    def setUp(self)
        user = User.objects.create(username='testuser')
        Task.objects.create(title='Task 1', status='new', user=user)
        Task.objects.create(title='Task 2', status='in_progress', user=user)
        Task.objects.create(title='Task 3', status='new', user=user)

    def test_status_counts(self)
        response = self.client.get('analytics')
        self.assertEqual(response.status_code, 200)
        self.assertIn('status_counts', response.context)
        status_counts = response.context['status_counts']
        self.assertTrue(any(item['status'] == 'new' and item['count'] == 2 for item in status_counts))
        self.assertTrue(any(item['status'] == 'in_progress' and item['count'] == 1 for item in status_counts))

