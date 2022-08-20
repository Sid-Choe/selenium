from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(
    ChromeDriverManager().install(), options=chrome_options)


browser.get("https://google.com")

search_bar = browser.find_element(By.CLASS_NAME, "gLFyf")

search_bar.send_keys("hello")
search_bar.send_keys(Keys.ENTER)
search_results = browser.find_elements(By.CLASS_NAME, "MjjYud")

print(search_results)
