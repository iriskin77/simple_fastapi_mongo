from fastapi import APIRouter
#from .students.handlers import router
import students.handlers as r

routes = APIRouter()

routes.include_router(router=r.router, prefix="/students", tags=["student"])
