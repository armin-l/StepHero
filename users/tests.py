from django.test import TestCase
from django.contrib.auth.models import User
from users.models import Group

class GroupCreationTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_group_creation(self):
        # Ensure groups can only be created by authenticated users
        self.client.login(username='testuser', password='testpass')
        response = self.client.post('/group/create/', {
            'name': 'Fitness Warriors',
            'description': 'A group of fitness enthusiasts'
        })
        
        # Check redirection to group page or success response
        self.assertEqual(response.status_code, 302)
        
        # Validate that the group was created in the database
        group = Group.objects.get(name='Fitness Warriors')
        self.assertEqual(group.owner, self.user)
