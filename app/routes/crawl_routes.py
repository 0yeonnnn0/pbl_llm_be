# API 라우트 정의
from fastapi import APIRouter
from app.models.crawl_models import CrawlRequest, CrawlResponse
from app.services.crawler.selenium_crawler import get_html_with_selenium
from app.controllers.boj_controller import process_problem

router = APIRouter()


@router.post("/crawl", response_model=CrawlResponse)
async def crawl(request: CrawlRequest):
    print(f"🥕🥕🥕 자 문제 URL 들어왔다 🥕🥕🥕: {request.url}")
    # 1. URL에서 HTML str 형태로 가져오기
    html = await get_html_with_selenium(str(request.url))
    # 2. HTML에서 데이터 추출 및 해설 불러오기
    result = await process_problem(html)
    print(f"🥕🥕🥕 자 문제 해설 가져왔다 🥕🥕🥕: {result}")
    # 3. 결과 반환
    return {"url": str(request.url), "data": str(result)}
