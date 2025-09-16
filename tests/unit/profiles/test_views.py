import pytest
from django.test import Client
from django.urls import reverse
from bs4 import BeautifulSoup


@pytest.mark.django_db
def test_view_should_display_right_len_list(sample_profile):
    """
    test that html page displays the right amount of objects
    created by fixture
    """
    c = Client()
    url = reverse('profiles_index')
    response = c.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    li_tags = soup.find_all('li')
    assert len(li_tags) == 3

@pytest.mark.django_db
def test_detail_view_with_wrong_username_should_be_catched(sample_profile):
    """
    test if an unknown username in qstring is well redirected
    """
    c = Client()
    url = reverse('profile', kwargs={"username": "testtest"})
    response = c.get(url)
    assert response['Location'] == reverse('profiles_index')
