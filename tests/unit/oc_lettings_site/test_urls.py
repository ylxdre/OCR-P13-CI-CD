from django.urls import reverse, resolve
from oc_lettings_site.views import index
from django.test import Client


def test_server_should_answer_200():
    """ test the server's response on home """
    c = Client()
    url = reverse('index')
    response = c.get(url)
    assert response.status_code == 200


def test_home_url():
    """ test the home url """
    url = reverse('index')
    assert resolve(url).view_name == 'index'
    assert resolve(url).func, index()