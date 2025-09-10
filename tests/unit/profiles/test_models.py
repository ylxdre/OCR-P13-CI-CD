import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_str_profile():
    user = User.objects.create(
        username='TestUser',
        password='password',
    )
    profile = Profile.objects.create(
        user=user,
        favorite_city="Paris",
    )
    assert str(profile) == "TestUser"
