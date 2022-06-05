from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from strawberry.asgi import GraphQL
from api.schema import schema

DATABASE_URL = "sqlite:////home/busayor/Shiii/FastAPI/torotise-orm/app/test.db"
# DATABASE_URL = "postgres://postgres:@127.0.0.1:5432/test_db"

app = FastAPI()

graphql_app = GraphQL(schema)
app.add_route("/analytics", graphql_app)
app.add_websocket_route("/analytics", graphql_app)

register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["main.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
