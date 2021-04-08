import pytest
from django.test import Client

from .models import HashGenerator, UrlKeeper
from .base_int_operation import number_to_str

# Create your tests here.
from django.urls import reverse


@pytest.mark.django_db
def test_get_create_shortened_url():
    c = Client()
    response = c.get(reverse('create_shortened_url'))
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize("url", ["http://www.wp.pl", "https://onet.com", "http://kajak.pl", ])
def test_get_create_shortened_url(url):
    c = Client()
    hg = HashGenerator.get_generator()
    response = c.post(reverse('create_shortened_url', ), {'original': url})
    assert response.status_code == 302
    url_keeper = UrlKeeper.objects.last()
    assert int(url_keeper.shortened, HashGenerator.BASE) == int(hg.current_value, HashGenerator.BASE) + 1
