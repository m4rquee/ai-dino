import time
from timeit import default_timer as timer

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def get_score():
    return driver.execute_script('return Runner().distanceRan')


def start_game(actions):
    actions.send_keys(Keys.SPACE)
    actions.perform()


def crashed(driver):
    return driver.execute_script('return Runner().crashed')


def run_loop(driver, actions):
    while not crashed(driver):
        actions.send_keys(Keys.ARROW_UP)
        actions.perform()
        time.sleep(0.1)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--start-maximized')

driver = webdriver.Chrome('/home/lucas.silva/projects/ai-dino/chromedriver',
                          options=chrome_options)  # Optional argument, if not specified will search path.
driver.get('chrome://dino')

print('Starting session!')

actions = ActionChains(driver)

for i in range(10):
    print('Starting %ith game' % i)
    start_game(actions)
    start = timer()
    run_loop(driver, actions)
    print('Score:', timer() - start)

driver.quit()

print('Game session')
