from enum import Enum

import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL


@strawberry.enum
class Permission(Enum):
    READ = "READ"
    WRITE = "WRITE"


@strawberry.type
class Service:
    name: str
    version: str
    schema: str


@strawberry.type
class Query:
    @strawberry.field
    def permission2(self) -> Permission:
        return Permission.WRITE

    @strawberry.field
    def service(self) -> Service:
        return Service(
            name="service2",
            version="1.0.0",
            schema=SERVICE_SDL or "Schema not available",
        )


schema = strawberry.Schema(query=Query)
SERVICE_SDL = schema.as_str()

graphql_app = GraphQL(schema)
app = FastAPI()
app.add_route("/graphql", graphql_app)
print(SERVICE_SDL)
