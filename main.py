import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--start-maximized')

driver = webdriver.Chrome('/home/lucas.silva/projects/ai-dino/chromedriver',
                          options=chrome_options)  # Optional argument, if not specified will search path.
driver.get('chrome://dino')

actions = ActionChains(driver)
actions.send_keys(Keys.SPACE)
actions.perform()

for _ in range(10 ** 6):
    actions.send_keys(Keys.ARROW_UP)
    actions.perform()
    time.sleep(0.1)

driver.quit()
