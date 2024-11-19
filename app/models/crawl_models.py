# 데이터 모델 정의 (Pydantic 사용)
from pydantic import BaseModel, HttpUrl


class CrawlRequest(BaseModel):
    url: HttpUrl


class CrawlResponse(BaseModel):
    url: str
    data: str
