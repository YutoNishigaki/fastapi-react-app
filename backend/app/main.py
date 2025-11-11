from fastapi import FastAPI
from app.api.top_router import api_router

app = FastAPI(
    title="FastAPI App",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api")

# ヘルスチェック
@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}