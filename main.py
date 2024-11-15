from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from src.utils.dbUtil import engine
from src import models
from src.routers import products, categorys, brands, auth
import uvicorn
## ---- Create Database ---
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization"],
)

## ------- Routers -------
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(categorys.router)
app.include_router(brands.router)

add_pagination(app)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)