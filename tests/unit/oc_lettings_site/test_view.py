from django.test import Client
from django.urls import reverse


def test_view_should_reply_title_on_home():
    """ test the content display (title) """
    c = Client()
    url = reverse('index')
    response = c.get(url)
    assert "Welcome to Holiday Homes</h1>" in response.content.decode()
