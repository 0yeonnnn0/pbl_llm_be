import os
import httpx
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


async def problem_analysis(question: str) -> dict:
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }

    messages = [
        {
            "role": "system",
            "content": "너는 코딩테스트를 세상에서 가장 잘 푸는 사람이야.",
        },
        {
            "role": "user",
            "content": (
                f"문제의 제목은 {question['title']}이고 문제의 내용은 다음과 같아: {question['description']}.\n"
                f"이 문제의 입력 조건은 다음과 같아: {question['input']}.\n"
                f"이 문제의 출력 조건은 다음과 같아: {question['output']}.\n"
                "이 문제에 대한 해설을 해줄 수 있니? 아래의 단계를 참고해주세요.\n"
                "1. 단계별로 분석하기, 2. 단계별로 어떤 자료구조나 알고리즘을 사용하는지 3. 시간복잡도와 공간복잡도.\n"
                "4. 코드 예시는 수도 코드를 활용해서 작성해줘."
            ),
        },
    ]

    payload = {
        "model": "gpt-4",
        "messages": messages,
        "max_tokens": 5000,
        "temperature": 1.0,
    }

    async with httpx.AsyncClient(timeout=100) as client:
        response = await client.post(
            "https://api.openai.com/v1/chat/completions", json=payload, headers=headers
        )
        if response.status_code != 200:
            return {"error": response.json().get("error", "Unknown error")}
        return response.json()
