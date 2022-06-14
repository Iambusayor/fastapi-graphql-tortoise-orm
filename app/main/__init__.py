from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from strawberry.asgi import GraphQL
import strawberry
from api.query import Query
from api.mutation import Mutation

DATABASE_URL = "postgres://postgres:password@127.0.0.1:5432/test"


def init(app: FastAPI):
    register_tortoise(
        app,
        db_url=DATABASE_URL,
        modules={"models": ["main.models", "aerich.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )


def switch_to_test_mode():
    global TORTOISE_ORM, generate_schemas
    TORTOISE_ORM["connections"][
        "default"
    ] = "postgres://postgres:password@127.0.0.1:5432/test_{}"
    generate_schemas = True


TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["main.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}

app = FastAPI()

init(app)

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQL(schema)
app.add_route("/analytics", graphql_app)
app.add_websocket_route("/analytics", graphql_app)
