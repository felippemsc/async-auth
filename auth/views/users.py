from aiohttp import web

from webargs.aiohttpparser import use_args

from auth.models.users import User
from auth.schemas.users import UserSchema


class UserView(web.View):
    schema = UserSchema()
    model = User

    @use_args(UserSchema)
    async def post(self, user):
        user_dict = await self.schema.new_key(user)
        user = await self.model.objects.create(**user_dict)
        return web.json_response(self.schema.dump(user))

    async def get(self):
        users = await self.model.objects.all()
        return web.json_response({"users": UserSchema(many=True).dump(users)})
