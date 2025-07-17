from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .daypoint import login 
import time
import tempfile 

from selenium.common.exceptions import NoSuchElementException

def readpoint_get():
    # Chromeドライバー
    driver = webdriver.Chrome()
    
    # ログイン
    login(driver)
    
    #タイトル
    title = "読んで貯める"
    element = driver.find_element(By.XPATH, f'//span[text()="{title}"]')
    element.click()
    
    #実施
    elements = driver.find_elements(By.CSS_SELECTOR, 'a[href="atpress/"]')
    #text = "クリックで1pt"

    for i, element in enumerate(elements):
        #if element.text ==  text:
            print(f"{i}番目: ")
            element.click()
            time.sleep(2)