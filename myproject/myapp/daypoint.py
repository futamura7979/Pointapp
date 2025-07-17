from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import tempfile 
import shutil 

from selenium.common.exceptions import NoSuchElementException

def run_selenium_script():
    tmpdirname = tempfile.mkdtemp()  # ここで1回だけ作る
    print(f"セレニウム用一時ディレクトリ: {tmpdirname}")

    try:
        # Chromeオプション設定
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920,1080')
        options.add_argument(f'--user-data-dir={tmpdirname}')

        print("エラー５直前")
        driver = webdriver.Chrome(options=options)
        print("セレニウムヘッドレスモード起動")

        login(driver)

        title = "毎日クリック"
        element = driver.find_element(By.XPATH, f'//span[text()="{title}"]')
        element.click()

        elements = driver.find_elements(By.CSS_SELECTOR, ".go_btn")
        for i, element in enumerate(elements):
            if element.text == "クリックで1pt":
                print(f"{i}番目: {element.text}")
                element.click()
                time.sleep(2)

        driver.quit()
        print("ドライバーシャットダウン完了")

    finally:
        # エラーの有無に関係なく一時ディレクトリを削除
        shutil.rmtree(tmpdirname)
        print(f"一時ディレクトリ {tmpdirname} を削除しました")

def login(driver1):
    print("ログイン開始")
    
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
    print("ログイン完了")