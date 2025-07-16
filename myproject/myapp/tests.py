from django.test import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#import chromedriver_binary


def test_selenium_script():

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    driver.get('https://www.google.co.jp')

    print(driver.page_source)