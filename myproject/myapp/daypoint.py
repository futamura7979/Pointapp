from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import tempfile 
import shutil 
import glob, shutil

from selenium.common.exceptions import NoSuchElementException

def run_selenium_script():
    print("セレニウム起動完了")
    
    # 古い一時ディレクトリ削除
    # for d in glob.glob("/tmp/selenium_*"):
    #     try:
    #         shutil.rmtree(d)
    #     except Exception as e:
    #         print(f"削除失敗: {d} - {e}")
    
    # ✅ 新しい一時ディレクトリ作成
    # tmpdirname = tempfile.mkdtemp(prefix="selenium_")
    # print(f"使用する一時ディレクトリ: {tmpdirname}")
    
    # Chromeオプション設定
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # ヘッドレスモード
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')
    # options.add_argument(f'--user-data-dir={tmpdirname}')  # 毎回ユニークなディレクトリを使う
    
    print("エラー５")
    driver = webdriver.Chrome(options=options)
    
    print("セレニウムヘッドレスモード")
    # Chromeドライバー
    #driver = webdriver.Chrome()
    
    # ログイン
    login(driver)
    
    #タイトル
    title = "毎日クリック"
    element = driver.find_element(By.XPATH, f'//span[text()="{title}"]')
    element.click()
    

    elements = driver.find_elements(By.CSS_SELECTOR, ".go_btn")
    text = "クリックで1pt"

    for i, element in enumerate(elements):
        if element.text ==  text:
            print(f"{i}番目: {element.text}")
            element.click()
            time.sleep(2)
    
    #ドライバーシャットダウン
    driver.quit()
    print("ドライバーシャットダウン完了")
    



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