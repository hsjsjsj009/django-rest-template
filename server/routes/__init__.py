from ninja import NinjaAPI
from server.middlewares.auth import JWTBearer
import server.routes.example

v1_route = NinjaAPI(auth=JWTBearer(), version="1.0.0")
v1_route.add_router('example', example.router)
