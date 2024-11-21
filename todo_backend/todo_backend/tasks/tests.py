import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_create_task():
    user = User.objects.create_user(username='testuser', password='password')
    client = APIClient()
    client.force_authenticate(user=user)

    response = client.post('/api/tasks/', {'title': 'Test Task', 'description': 'Test Description'})
    assert response.status_code == 201
