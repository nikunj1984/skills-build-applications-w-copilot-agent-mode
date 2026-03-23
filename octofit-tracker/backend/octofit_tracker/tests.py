from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import User, Team, Activity, Workout, Leaderboard

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.team = Team.objects.create(name='Test Team')
        self.team.members.add(self.user)
        self.activity = Activity.objects.create(user=self.user, activity_type='run', duration=30, points=10)
        self.workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        self.workout.suggested_for.add(self.user)
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=10, month='March')

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, 200)

    def test_user_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_team_list(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)

    def test_activity_list(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)

    def test_workout_list(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_list(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, 200)
