import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

async def get_html_with_selenium(url: str) -> str:
    """
    Selenium을 사용하여 주어진 URL의 HTML을 비동기적으로 가져오는 함수
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
        
        # AWS WAF 우회를 위한 추가 설정
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

    def _get_html_sync():
        try:
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            WebDriverWait(driver, 10).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            return driver.page_source
        finally:
            driver.quit()
    
    return await asyncio.to_thread(_get_html_sync)

# async def main():
#     result = await get_html_with_selenium("https://www.acmicpc.net/problem/1002")
#     print(result)

# if __name__ == "__main__":
#     asyncio.run(main())