import asyncpg
from asyncpg import Pool, Record
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import Response, JSONResponse


async def create_database_pool() -> None:
    pool: Pool = await asyncpg.create_pool(
        host='127.0.0.1',
        port=5439,
        user='postgres',
        password='password',
        database='products',
        min_size=6,
        max_size=6
    )

    app.state.DB = pool


async def destroy_database_pool() -> None:
    await app.state.close()


async def brands(request: Request) -> Response:
    connection: Pool = request.app.state.DB
    query = 'SELECT brand_id, brand_name FROM brand;'
    results: list[Record] = await connection.fetch(query)
    result_as_dict: list[dict] = [dict(brand) for brand in results]
    return JSONResponse(result_as_dict)


app = Starlette(
    routes=[Route('/brands', brands)],
    on_startup=[create_database_pool],
    on_shutdown=[destroy_database_pool]
)