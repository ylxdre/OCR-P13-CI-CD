import pytest
from lettings.models import Address, Letting

from django.test import Client
from django.urls import reverse
from bs4 import BeautifulSoup


@pytest.mark.django_db
def test_view_should_display_right_len_list(sample_letting):
    """
    test if the list displayed contains the right amount of objects
    created in fixture
    """
    c = Client()
    url = reverse('lettings_index')
    response = c.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    li_tags = soup.find_all('li')
    assert len(li_tags) == 2

@pytest.mark.django_db
def test_detail_view_should_display_right_title(sample_letting):
    """
    test if the detail view displays well the first object
    """
    c = Client()
    url = reverse('letting', kwargs={'letting_id': 1})
    response = c.get(url)
    assert "Pretty thing" in response.content.decode()

@pytest.mark.django_db
def test_detail_view_wrong_id_should_be_catched(sample_letting):
    """
    test if an unknown id raises the right behavior
    """
    c = Client()
    url = reverse('letting', kwargs={'letting_id': 10})
    response = c.get(url)
    assert response['Location'] == reverse('lettings_index')
