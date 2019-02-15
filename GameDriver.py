import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GameDriver(webdriver.Chrome):
    def __init__(self, executable_path='./chromedriver'):
        self.chrome_options = webdriver.ChromeOptions()
        # self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--mute-audio')
        self.chrome_options.add_argument('--disable-extensions')
        self.chrome_options.add_argument('--window-size=720,480')

        super().__init__(executable_path, options=self.chrome_options)
        self.actions = webdriver.ActionChains(self)
        super().get('https://chromedino.com/')

    def get_game_prop(self, prop):
        return super().execute_script('return window.Runner()["%s"]' % prop)

    def send_key(self, key=Keys.ARROW_UP):
        self.actions.send_keys(key)
        self.actions.perform()

    def take_screenshot(self, by=By.CLASS_NAME, value='runner-canvas'):
        return self.find_element(by, value).screenshot_as_png

    def run_loop(self):
        time.sleep(1)
        self.send_key()
        time.sleep(3.5)

        while not self.get_game_prop('crashed'):
            self.send_key()
            yield self.take_screenshot()
            time.sleep(0.1)
