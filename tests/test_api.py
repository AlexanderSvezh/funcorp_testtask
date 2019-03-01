import requests
import pytest


# example test for random open api

api_url = 'https://jsonplaceholder.typicode.com'
api_url_new = 'https://reqres.in/api'


def get_response(type, num):
    url = '{}/{}/{}'.format(api_url_new, type, num)
    resp = requests.get(url)
    print(resp.json())
    return resp.json()


def data_generate():
    for i in range(1, 6):
        yield i


@pytest.mark.parametrize('num', data_generate())
def test_posts(num):
    assert get_response('posts', num)


@pytest.mark.parametrize('num', data_generate())
def test_books(num):
    assert get_response('books', num)


@pytest.mark.parametrize('num', data_generate())
def test_users(num):
    x = get_response('users', num)
    print('\n{}'.format(x['data']['first_name']))
