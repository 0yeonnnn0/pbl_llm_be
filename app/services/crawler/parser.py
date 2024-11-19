# HTML 데이터 파싱

from bs4 import BeautifulSoup


def parse_html_BOJ(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")

    # 예시: 제목과 메타 설명 추출
    title = soup.title.string if soup.title else "No Title"
    description_div = soup.find("div", id="problem_description")
    input_div = soup.find("div", id="problem_input")
    output_div = soup.find("div", id="problem_output")

    description_text = get_text(description_div)
    input_text = get_text(input_div)
    output_text = get_text(output_div)

    return {
        "title": title,
        "description": description_text,
        "input": input_text,
        "output": output_text,
    }


# HTML 데이터 에서 텍스트만 가져옴
def get_text(div):
    text = div.get_text(strip=True) if div else "No Description"
    return text
