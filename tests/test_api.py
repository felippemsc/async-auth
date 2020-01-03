# -*- coding: utf-8 -*-
from datetime import datetime


class TestRoot:
    async def test_health_check(self, client):
        result = await client.get('/')
        resp_json = await result.json()

        assert resp_json['status'] == 'Ok'
        assert result.status == 200


class TestCreateUser:
    async def test_short_password(self, client):
        user_dict = {
            'email': 'abc@abc.com',
            'password': '123456'
        }

        result = await client.post('/user', data=user_dict)
        resp_json = await result.json()

        assert resp_json['errors'] == {'password': ['Length must be between 8 and 20.']}
        assert result.status == 422

    async def test_long_password(self, client):
        user_dict = {
            'email': 'abc@abc.com',
            'password': '123456789012345678901234567890'
        }

        result = await client.post('/user', data=user_dict)
        resp_json = await result.json()

        assert resp_json['errors'] == {'password': ['Length must be between 8 and 20.']}
        assert result.status == 422

    async def test_password_without_digit(self, client):
        user_dict = {
            'email': 'abc@abc.com',
            'password': 'abcdefghi'
        }

        result = await client.post('/user', data=user_dict)
        resp_json = await result.json()

        assert resp_json['errors'] == {'password': ['Must have at least one numeral.']}
        assert result.status == 422

    async def test_password_without_uppercase_letter(self, client):
        user_dict = {
            'email': 'abc@abc.com',
            'password': 'abcd1234'
        }

        result = await client.post('/user', data=user_dict)
        resp_json = await result.json()

        assert resp_json['errors'] == {'password': ['Must have at least one uppercase letter.']}
        assert result.status == 422

    async def test_password_without_lowercase_letter(self, client):
        user_dict = {
            'email': 'abc@abc.com',
            'password': 'ABCD1234'
        }

        result = await client.post('/user', data=user_dict)
        resp_json = await result.json()

        assert resp_json['errors'] == {'password': ['Must have at least one lowercase letter.']}
        assert result.status == 422

    async def test_password_without_symbols(self, client):
        user_dict = {
            'email': 'abc@abc.com',
            'password': 'abCD1234'
        }

        result = await client.post('/user', data=user_dict)
        resp_json = await result.json()

        assert resp_json['errors'] == {'password': ['Must have at least one of the symbols !$@#%&*/?;:|][}{~^']}
        assert result.status == 422

    async def test_invalid_email(self, client):
        user_dict = {
            'email': 'abc',
            'password': 'abCD1234!!!'
        }

        result = await client.post('/user', data=user_dict)
        resp_json = await result.json()

        assert resp_json['errors'] == {'email': ['Not a valid email address.']}
        assert result.status == 422

    async def test_success(self, client):
        user_dict = {
            'email': 'abc@abc.com',
            'password': 'aBc123!!!'
        }

        result = await client.post('/user', data=user_dict)
        resp_json = await result.json()

        expected_response = {
            'email': 'abc@abc.com',
            'id': 1,
            'updated_at': None,
        }

        assert len(resp_json.pop('key')) == 8
        assert datetime.now() > datetime.strptime(resp_json.pop('created_at'), '%Y-%m-%dT%H:%M:%S.%f')
        assert resp_json == expected_response
        assert result.status == 201

    async def test_email_already_exists(self, client):
        user_dict = {
            'email': 'abc@abc.com',
            'password': 'aBc123!!!'
        }

        result = await client.post('/user', data=user_dict)

        assert result.status == 201

        result = await client.post('/user', data=user_dict)
        resp_json = await result.json()
        print(resp_json)

        assert resp_json['msg'] == 'E-mail already exists'
        assert result.status == 400
