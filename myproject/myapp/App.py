from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import tempfile 

from selenium.common.exceptions import NoSuchElementException

def run_selenium_script():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # ヘッドレスモード
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')  # ウィンドウサイズ拡張
    options.add_argument(f'--user-data-dir={tempfile.mkdtemp()}') 
    
    

    # Chromeドラ
    # driver = webdriver.Chrome()
    
    # ← ヘッドレスオプションを反映させる！
    driver = webdriver.Chrome(options=options)

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


    element = driver.find_element(By.XPATH, '//span[text()="毎日クリック"]')
    element.click()


    elements = driver.find_elements(By.CSS_SELECTOR, ".go_btn")
    text = "クリックで1pt"



    for i, element in enumerate(elements):
        if element.text ==  text:
            print(f"{i}番目: {element.text}")
            element.click()
            time.sleep(2)
            
            
            
