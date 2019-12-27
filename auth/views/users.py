from aiohttp import web

from webargs.aiohttpparser import use_args

from auth.models.users import User, EmailAlreadyExists
from auth.schemas import QueryStringSchema
from auth.schemas.users import UserSchema
from auth.utils import Pagination


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

    @use_args(QueryStringSchema, locations=("querystring",))
    async def get(self, query_params):
        pagination = Pagination(**query_params)
        users = await self.model.get_many(
            limit=pagination.limit, offset=pagination.offset
        )

        response_body = {
            "count": await User.count(),
            "users": self.schema(many=True).dump(users),
        }
        if response_body["count"] > len(response_body["users"]):
            return web.json_response(response_body, status=206)

        return web.json_response(response_body, status=200)
