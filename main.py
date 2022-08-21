from re import search
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


class GoogleKeywordScreenshooter:
    def __init__(self, keyword, screenshots_dir):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=chrome_options)
        self.keyword = keyword
        self.screenshots_dir = screenshots_dir

    def start(self):
        self.browser.get("https://google.com")
        search_bar = self.browser.find_element(By.CLASS_NAME, "gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)
        search_results = self.browser.find_elements(By.CLASS_NAME, "MjjYud")
        for index, result in enumerate(search_results):
            title = result.find_element(By.TAG_NAME, "h3")
            if title:
                result.screenshot(
                    f"{self.screenshots_dir}/{self.keyword}x{index}.png")

    def finish(self):
        self.browser.quit()


# 필요없는 부분 제외하고 싶은데 잘 안됨, 크롬 창에서 자바스크립트 이용 해당부분 삭제까지는 했는데 출력 하면 스크린샷이 삭제되기 전 까지만 찍히고 그 밑으로는 안찍힘
# tag name h3 안찾아진다고 하는거 같은데 잘 모르겠음 ㅠ

# except_results_1 = browser.find_elements(By.CLASS_NAME, "cUnQKe")

# except_results_2 = browser.find_elements(By.ID, "w3bYAd")

# except_results = except_results_1 + except_results_2
# for except_result in except_results:
#     browser.execute_script("""
#     const exception = arguments[0];
#     exception.parentElement.removeChild(exception)
#     """, except_result)
domain_competitors = GoogleKeywordScreenshooter("buy domain", "screenshots")
domain_competitors.start()
domain_competitors.finish()
python_competitors = GoogleKeywordScreenshooter("python book", "screenshots")
python_competitors.start()
python_competitors.finish()
