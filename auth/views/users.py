from aiohttp import web

from auth.models.users import UserModel


class UserView(web.View):
    async def post(self):
        saved_object = await UserModel.objects.create(email='teste@teste.com')
        return web.json_response({"hello": "world"})

    async def get(self):
        teste = await UserModel.objects.all()
        return web.json_response({"hello": "world"})
