from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from routes.user import user_route
from routes.order import order_route

app = FastAPI()

# app.include_router(order_route)
# app.include_router(user_route)
# app.include_router(order_route)


@app.exception_handler(Exception)
async def app_error_handler(request: Request, exc: Exception) -> JSONResponse:
    content = {"detail": str(exc)}
    return JSONResponse(status_code=500, content=content)

app.include_router(
    router=user_route,
    prefix='/user'
)

app.include_router(
    router=order_route,
    prefix='/order',
)