from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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


def login(driver1):
    driver = driver1
    # ログインページにアクセス
    driver.get("https://pointi.jp/entrance.php")

    time.sleep(1)

    # name=passとname=pass の属性をとって入力 
    email_input = driver.find_element(By.NAME, "email_address")
    email_input.send_keys("futamura.kunnren@gmail.com")

    pass_input = driver.find_element(By.NAME, "password")
    pass_input.send_keys("kikikiki")

    #クリック
    link = driver.find_element(By.NAME, "Submit")
    link.click()

    time.sleep(1)

    close_button = driver.find_element(By.ID, "cboxClose")
    close_button.click()