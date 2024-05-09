from fastapi import FastAPI, Body
import routes


app: FastAPI = FastAPI()
app.include_router(routes.routes)
