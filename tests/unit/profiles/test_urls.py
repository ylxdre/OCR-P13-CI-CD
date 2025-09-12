import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_should_get_200_on_profile_index():
    """ test the server's response on profile index page """
    c = Client()
    url = reverse('profiles_index')
    response = c.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_should_get_200_on_profile_detail(sample_profile):
    """ test the server's response on a profile detail page """
    c = Client()
    url = reverse('profile', kwargs={'username': "TestUser"})
    response = c.get(url)
    assert response.status_code == 200

