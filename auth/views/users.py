from aiohttp import web

from webargs.aiohttpparser import use_args

from auth.models.users import User, EmailAlreadyExists
from auth.schemas.users import UserSchema


class UserView(web.View):
    schema = UserSchema
    model = User

    @use_args(UserSchema)
    async def post(self, user_dict):
        try:
            user = await self.model.save(user_dict)
        except EmailAlreadyExists as err:
            raise web.HTTPBadRequest(text=err.msg)

        return web.json_response(self.schema().dump(user))

    async def get(self):
        users = await self.model.objects.all()
        return web.json_response({"users": self.schema(many=True).dump(users)})
