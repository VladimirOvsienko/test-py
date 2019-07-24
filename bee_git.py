from typing import Union
import os
from selenium import webdriver
import os
pytest_plugins  =  [ 'pytest_webdriver' ]
EXECUTABLE_PATH = '/home/vova/Progi/site/beekeeper/bee_test/chromedriver'
driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8000/')
print(driver.title)
assert driver.title == "Hello beekeeper"