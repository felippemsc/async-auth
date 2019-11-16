from aiohttp import web

from auth.models.users import User
from auth.schemas.users import UserSchema


class UserView(web.View):
    async def post(self):
        user_dict = await UserSchema().create({"email": "teste@teste.com"})
        user = await User.objects.create(**user_dict)
        user_dict = UserSchema().dump(user)
        return web.json_response(user_dict)

    async def get(self):
        users = await User.objects.all()
        return web.json_response({"users": UserSchema(many=True).dump(users)})
