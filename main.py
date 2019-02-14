import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome('/home/lucas.silva/projects/ai-dino/chromedriver',
                          options=chrome_options)  # Optional argument, if not specified will search path.
driver.get('https://chromedino.com/')
driver.quit()
