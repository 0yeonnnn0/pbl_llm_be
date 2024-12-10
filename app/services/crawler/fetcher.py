# HTTP 요청 및 HTML 가져오기
import httpx


async def fetch_html(url: str) -> str:

    # HTTP 요청 헤더 설정
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0.0.0 Safari/537.36"
        )
    }
    async with httpx.AsyncClient(headers=headers) as client:
        response = await client.get(url)
        response.raise_for_status()  # 요청 실패 시 예외 발생
        return response.text
