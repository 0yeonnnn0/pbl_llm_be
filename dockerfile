# Python 베이스 이미지
FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /app

# 종속성 파일 복사
COPY requirements.txt .

# 종속성 설치
RUN pip install --no-cache-dir -r requirements.txt

# FastAPI 앱 복사
COPY . .

# 패키지 경로 설정
ENV PYTHONPATH=/app

# Uvicorn 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]