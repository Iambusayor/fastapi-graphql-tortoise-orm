from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from strawberry.asgi import GraphQL
import strawberry
from api.query import Query

DATABASE_URL = "postgres://postgres:password@127.0.0.1:5432/test"
# DATABASE_URL = "postgres://postgres:@127.0.0.1:5432/test_db"

app = FastAPI()

schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)
app.add_route("/analytics", graphql_app)
app.add_websocket_route("/analytics", graphql_app)

register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["main.models", "aerich.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)


TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": ["main.models", "aerich.models"],
            "default_connection": "default",
        }
    },
}
