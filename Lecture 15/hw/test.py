import requests


def test_verify_response():
    response = requests.get('https://api.punkapi.com/v2/beers/8')

    assert response.status_code == 200
    assert response.json()[0]['name'] == 'Fake Lager'
    assert response.json()[0]['abv'] == 4.7


def test_wrong_request():
    response = requests.delete('https://api.punkapi.com/v2/beers/8')

    assert response.status_code == 404
    assert response.json()['message'] == 'No endpoint found that matches \'/v2/beers/8\''
