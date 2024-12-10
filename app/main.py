# FastAPI 엔트리 포인트
from fastapi import FastAPI
from app.routes.crawl_routes import router

app = FastAPI()

# API 라우트 등록
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}
