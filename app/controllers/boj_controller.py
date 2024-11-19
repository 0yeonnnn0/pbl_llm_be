# 안쓰는 파일

from fastapi import HTTPException
from app.services.crawler.parser import parse_html_BOJ
from app.services.openai_service import problem_analysis


# 문제 받아오기 및 OpenAI API 요청 처리
async def process_problem(html: dict):
    # 문제 텍스트 추출
    data = parse_html_BOJ(html)

    # OpenAI API 요청
    analysis = await problem_analysis(data)
    print(analysis)

    return analysis


# # 문제 ID 추출 및 API 요청 처리 - 지금은 사용하지 않음
# async def process_problem(data: dict):
#     """
#     클라이언트의 URL에서 문제 ID를 추출하고 API 요청
#     """
#     # Url 객체에서 문자열로 변환
#     url: AnyUrl = data.url  # URL 객체로 받음
#     if not url:
#         raise HTTPException(status_code=400, detail="URL is required")

#     # 문제 ID 추출
#     problem_id = parse_problem_id(str(url))
#     if not problem_id:
#         raise HTTPException(status_code=400, detail="Invalid URL format")

#     # 문제 세부 정보 가져오기
#     response = await fetch_problem_details(problem_id)
#     return response
