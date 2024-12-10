import re
import httpx


# URL에서 문제 ID를 추출
def parse_problem_id(url: str) -> str:
    match = re.search(r"/problem/(\d+)", url)
    if match:
        return match.group(1)  # 매칭된 숫자 그룹 반환
    return None


API_BASE_URL = "https://solved.ac/api/v3/problem/show"


# 백준 문제 불러오기 API
async def fetch_problem_details(problem_id: int) -> dict:
    """
    solved.ac API에 요청을 보내 문제 정보를 가져옴
    """
    print(f"Fetching problem details for ID: {problem_id}")
    print(f"API_BASE_URL: {API_BASE_URL}")
    params = {"problemId": problem_id}  # 쿼리 파라미터 설정
    headers = {
        "User-Agent": "FastAPI Client",  # 요청 차단 방지
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(API_BASE_URL, params=params, headers=headers)
        if response.status_code != 200:
            return {"error": f"Failed to fetch problem: {response.status_code}"}
        return response.json()
