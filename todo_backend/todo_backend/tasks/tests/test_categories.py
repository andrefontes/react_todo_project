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

@pytest.mark.django_db
def test_create_category(api_client, authenticate_user):
    url = reverse('category-list')
    data = {'name': 'New Category'}
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Category.objects.count() == 1
    assert Category.objects.get().name == 'New Category'

@pytest.mark.django_db
def test_list_categories(api_client, authenticate_user, category):
    url = reverse('category-list')
    response = api_client.get(url, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 1
    assert response.data['results'][0]['name'] == category.name

@pytest.mark.django_db
def test_update_category(api_client, authenticate_user, category):
    url = reverse('category-detail', args=[category.id])
    data = {'name': 'Updated Category'}
    response = api_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    category.refresh_from_db()
    assert category.name == 'Updated Category'

@pytest.mark.django_db
def test_delete_category(api_client, authenticate_user, category):
    url = reverse('category-detail', args=[category.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Category.objects.count() == 0
