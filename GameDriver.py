import time
import pyscreenshot as ImageGrab
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GameDriver(webdriver.Chrome):
    def __init__(self, executable_path='./chromedriver'):
        self.keys = [Keys.ARROW_UP, Keys.ARROW_DOWN, Keys.NULL]

        self.chrome_options = webdriver.ChromeOptions()
        # self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--mute-audio')
        self.chrome_options.add_argument('--disable-infobars')
        self.chrome_options.add_argument('--disable-extensions')
        self.chrome_options.add_argument('--window-size=720,480')

        super().__init__(executable_path, options=self.chrome_options)
        self.actions = webdriver.ActionChains(self)
        self.get('https://chromedino.com/')  # The default url doesn't work with headless

    def init(self):
        self.send_key()
        time.sleep(0.5)

    def get_game_prop(self, prop):
        return self.execute_script('return Runner.instance_["%s"]' % prop)

    def get_score(self):
        return self.get_game_prop('distanceRan')

    def restart(self):
        self.execute_script('Runner.instance_.restart()')
        time.sleep(3)

    def send_key(self, key=Keys.ARROW_UP):
        self.actions.send_keys(key)
        self.actions.perform()

    def take_screenshot(self):
        return ImageGrab.grab(bbox=(10, 10, 510, 510))

    def take_n_screenshot(self, n=4):
        for _ in range(n):
            yield self.take_screenshot()
            time.sleep(0.1)

    def run_loop(self):
        time.sleep(1)
        self.restart()

        key = Keys.ARROW_UP
        while not self.get_game_prop('playing'):
            self.send_key(key)
            key = yield self.take_n_screenshot()
            yield
