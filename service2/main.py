from asyncore import write
from enum import Enum

import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from strawberry.schema_directive import Location


@strawberry.schema_directive(name="common", locations=[Location.ENUM, Location.OBJECT])
class Common:
    pass


@strawberry.enum(directives=[Common()])
class Permission(Enum):
    WRITE = "WRITE"


@strawberry.type(directives=[Common()])
class AltPermission:
    write: bool


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
    def alt_permission2(self) -> AltPermission:
        return AltPermission(write=True)

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
