# API 라우트 정의
from fastapi import APIRouter
from app.models.crawl_models import CrawlRequest, CrawlResponse
from app.services.crawler.selenium_crawler import get_html_with_selenium
from app.controllers.boj_controller import process_problem

router = APIRouter()

print(" >>> 서버님 등장 <<<")

@router.post("/crawl", response_model=CrawlResponse, responses={
    200: {
        "description": "크롤링 및 GPT 분석 결과",
        "content": {
            "application/json": {
                "example": {
                    "url": "https://www.acmicpc.net/problem/1002",
                    "data": {
                        "id": "chatcmpl-AckCMbioa4pTzu3evivs8qROqEumT",
                        "object": "chat.completion",
                        "model": "gpt-4-0613",
                        "choices": [{
                            "message": {
                                "role": "assistant",
                                "content": "이 문제는 두 점에서 특정 거리에 있는 점들의 교집합을 구하는 문제입니다 어쩌구저쩌구..."
                            },
                            "finish_reason": "stop"
                        }],
                        "usage": {
                            "prompt_tokens": 686,
                            "completion_tokens": 743,
                            "total_tokens": 1429
                        }
                    }
                }
            }
        }
    }
})
async def crawl(request: CrawlRequest):
    print(f"🥕🥕🥕 자 문제 URL 들어왔다 🥕🥕🥕: {request.url}")
    # 1. URL에서 HTML str 형태로 가져오기
    html = await get_html_with_selenium(str(request.url))
    # 2. HTML에서 데이터 추출 및 해설 불러오기
    result = await process_problem(html)
    print(f"🥕🥕🥕 자 문제 해설 가져왔다 🥕🥕🥕: {result}")
    # 3. 결과 반환
    return {"url": str(request.url), "data": result}
