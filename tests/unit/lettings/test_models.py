import pytest


@pytest.mark.django_db
def test_address_str(sample_address):
    """ test if Address objects are well created """
    assert str(sample_address[0]) == "22 Quality Street"
    assert str(sample_address[1]) == "18 Rue Cocotte"


@pytest.mark.django_db
def test_letting_str2(sample_letting):
    """ test if Letting objects are well created """
    assert str(sample_letting[0]) == "Pretty thing"
    assert str(sample_letting[1]) == "Ugly thing"