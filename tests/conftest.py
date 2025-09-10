import pytest
from lettings.models import Address, Letting
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.fixture
@pytest.mark.django_db
def sample_address():
    """
    creates temporary Addresses objects in test DB
    :return: tuple of Address
    """
    address1 = Address.objects.create(
        number=22,
        street="Quality Street",
        city="New-York",
        state="New-York",
        zip_code=10010,
        country_iso_code="US"
    )
    address2 = Address.objects.create(
        number=18,
        street="Rue Cocotte",
        city="Paris",
        state="Ile-de-France",
        zip_code=75000,
        country_iso_code="FR"
    )
    return address1, address2


@pytest.fixture
@pytest.mark.django_db
def sample_letting(sample_address):
    """
    creates temporary Letting objects in test DB
    :return: tuple of Lettings
    """
    letting = Letting.objects.create(
        title="Pretty thing",
        address=sample_address[0],
    )
    letting2 = Letting.objects.create(
        title="Ugly thing",
        address=sample_address[1],
    )

    return letting, letting2


@pytest.fixture
@pytest.mark.django_db
def sample_profile():
    """
    creates temporary Profile objects in test DB
    :return: tuple of Profiles
    """
    user = User.objects.create(
        username='TestUser',
        password='password',
    )
    user2 = User.objects.create(
        username='TestUser2',
        password='password2',
    )
    user3 = User.objects.create(
        username='TestUser3',
        password='password2',
    )
    profile = Profile.objects.create(
        user=user,
        favorite_city="Paris",
    )
    profile2 = Profile.objects.create(
        user=user2,
        favorite_city="Marseilles",
    )
    profile3 = Profile.objects.create(
        user=user3,
        favorite_city="Rennes",
    )
    return profile, profile2, profile3
