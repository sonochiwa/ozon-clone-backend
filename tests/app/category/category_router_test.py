from tests import test_client


def test_read_category_by_id():
    response = test_client.get('/api/categories/1')

    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'name': 'Электроника',
    }
