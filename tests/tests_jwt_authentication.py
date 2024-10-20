import pytest


@pytest.mark.django_db
def test_token_obtain_pair(api, main_user):
    response = api.post('/api/token/',
                        {
                            'username': "username",
                            'password': "password"
                        },
                        format='json',
                        expected_status_code=200
                        )

    assert 'access' in response
    assert 'refresh' in response


@pytest.mark.django_db
def test_token_refresh(api, main_user):
    token_response = api.post('/api/token/',
                              {
                                  'username': "username",
                                  'password': "password"
                              },
                              format='json',
                              expected_status_code=200
                              )
    refresh_token = token_response['refresh']

    refresh_response = api.post('/api/token/refresh/',
                                {'refresh': refresh_token},
                                format='json',
                                expected_status_code=200
                                )

    assert 'access' in refresh_response
