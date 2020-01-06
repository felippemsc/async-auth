

class TestMiddleware:
    async def test_unexpected_code(self, mid_client):
        resp = await mid_client.get('/unexpected')

        assert resp.status == 444

    async def test_unauthorized(self, mid_client):
        resp = await mid_client.get('/unauthorized')
        resp_json = await resp.json()

        assert resp_json['msg'] == 'Unauthorized'
        assert resp.status == 401

    async def test_not_found(self, mid_client):
        resp = await mid_client.get('/not-found')
        resp_json = await resp.json()

        assert resp_json['msg'] == 'Testing Not Found'
        assert resp.status == 404

    async def test_client_closed_request(self, mid_client):
        resp = await mid_client.get('/client-closed')
        resp_json = await resp.json()

        assert resp_json['msg'] == 'Client Closed Request'
        assert resp.status == 499

    async def test_exception(self, mid_client):
        resp = await mid_client.get('/exception')
        resp_json = await resp.json()

        assert resp_json['msg'] == 'BroadException: Hello, I`m an Exception'
        assert resp.status == 500
