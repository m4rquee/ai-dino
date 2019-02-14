from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GameDriver(webdriver.Chrome):
    def __init__(self, executable_path='./chromedriver'):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--start-maximized')
        self.chrome_options.add_argument('--disable-extensions')

        super().__init__(executable_path, options=self.chrome_options)
        self.actions = webdriver.ActionChains(self)
        self.get()

    def get(self, url='chrome://dino'):
        super().get(url)

    def get_game_prop(self, prop):
        return super().execute_script('return window.Runner()["%s"]' % prop)

    def send_key(self, key=Keys.ARROW_UP):
        self.actions.send_keys(key)
        self.actions.send_keys(key)
        self.actions.send_keys(key)
        self.actions.send_keys(key)
        self.actions.send_keys(key)
        self.actions.send_keys(key)
        self.actions.send_keys(key)
        self.actions.perform()

    def run_loop(self):
        while not self.get_game_prop('crashed'):
            self.send_key()
