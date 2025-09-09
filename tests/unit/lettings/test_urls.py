import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_should_get_200_on_lettings_index():
    """ test the server's response """
    c = Client()
    url = reverse('lettings_index')
    response = c.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_should_get_200_on_letting_detail(sample_letting):
    c = Client()
    url = reverse('letting', kwargs={'letting_id':1})
    response = c.get(url)
    assert response.status_code == 200

