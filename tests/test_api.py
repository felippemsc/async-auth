# -*- coding: utf-8 -*-


class TestAPI:
    async def test_health_check(self, client):
        result = await client.get('/')
        resp_json = await result.json()
        assert resp_json['status'] == 'Ok'
        assert result.status == 200
