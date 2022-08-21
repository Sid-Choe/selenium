import os
from base64 import urlsafe_b64decode
from math import ceil
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class ResponsiveTester:
    def __init__(self, urls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()), options=chrome_options)
        self.urls = urls
        self.browser.maximize_window()
        self.sizes = [480, 960, 1366]
        self.os = os

    def screenshot(self, url, folder_name):
        SCREEN_HEIGHT = 875
        self.browser.get(url)
        self.browser.maximize_window()

        for size in self.sizes:
            self.browser.set_window_size(size, SCREEN_HEIGHT)
            self.browser.execute_script("window.scrollTo(0,0)")
            time.sleep(3)
            scroll_size = self.browser.execute_script(
                "return document.body.scrollHeight")
            inner_size = self.browser.execute_script(
                "return window.innerHeight")
            scroll_times = ceil(scroll_size / inner_size)

            for times in range(scroll_times):
                self.browser.save_screenshot(
                    f"screenshots/{folder_name}/{folder_name}_{size}x{times+1}.png")
                self.browser.execute_script(
                    f"window.scrollTo(0, {(times+1)} * {inner_size-64})")

    def start(self):
        for url in self.urls:
            folder_name = url[8:]
            try:
                if not os.path.exists(folder_name):
                    self.os.mkdir(f"screenshots/{folder_name}")
                    self.screenshot(url, folder_name)
            except:
                self.screenshot(url, folder_name)

    def finish(self):
        self.browser.quit()


urls = ["https://google.com", "https://naver.com", "https://nomadcoders.co"]
tester = ResponsiveTester(urls)
tester.start()
tester.finish()
