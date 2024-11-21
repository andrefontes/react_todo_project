import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from tasks.models import Task, Category
from django.contrib.auth.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    return User.objects.create_user(username='testuser', password='testpass')

@pytest.fixture
def authenticate_user(api_client, create_user):
    api_client.login(username='testuser', password='testpass')
    return create_user

@pytest.fixture
def category():
    return Category.objects.create(name="Test Category")

@pytest.fixture
def task(category):
    return Task.objects.create(title="Test Task", category=category, completed=False)

@pytest.mark.django_db
def test_create_task(api_client, authenticate_user, category):
    url = reverse('task-list')
    data = {
        'title': 'New Task',
        'category': category.id,
        'completed': False
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Task.objects.count() == 1
    assert Task.objects.get().title == 'New Task'

@pytest.mark.django_db
def test_list_tasks(api_client, authenticate_user, task):
    url = reverse('task-list')
    response = api_client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['title'] == task.title

@pytest.mark.django_db
def test_update_task(api_client, authenticate_user, task):
    url = reverse('task-detail', args=[task.id])
    data = {
        'title': 'Updated Task',
        'category': task.category.id,
        'completed': True
    }
    response = api_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    task.refresh_from_db()
    assert task.title == 'Updated Task'
    assert task.completed is True

@pytest.mark.django_db
def test_delete_task(api_client, authenticate_user, task):
    url = reverse('task-detail', args=[task.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Task.objects.count() == 0
