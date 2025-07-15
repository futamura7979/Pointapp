from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options  # ← 追加

def run_selenium_script():
    # ヘッドレスモードの設定
    options = Options()
    options.add_argument('--headless')  # ヘッドレスモード
    options.add_argument('--disable-gpu')  # GPU無効（必須ではないが安定性UP）
    options.add_argument('--no-sandbox')  # サンドボックス無効化
    options.add_argument('--disable-dev-shm-usage')  # 一時ファイルの使用制限回避
    options.add_argument('--window-size=1280x800')  # 必要に応じて指定

    # Chromeドライバーを起動（オプション付き）
    driver = webdriver.Chrome(options=options)

    # ログインページにアクセス
    driver.get("https://pointi.jp/entrance.php")
    time.sleep(1)

    # メールアドレスとパスワードを入力
    email_input = driver.find_element(By.NAME, "email_address")
    email_input.send_keys("futamura.kunnren@gmail.com")

    pass_input = driver.find_element(By.NAME, "password")
    pass_input.send_keys("kikikiki")

    # ログインボタンクリック
    link = driver.find_element(By.NAME, "Submit")
    link.click()
    time.sleep(1)

    # ポップアップを閉じる
    try:
        close_button = driver.find_element(By.ID, "cboxClose")
        close_button.click()
        time.sleep(1)
    except NoSuchElementException:
        print("ポップアップが見つかりませんでした")

    # 「毎日クリック」リンクを探してクリック
    element = driver.find_element(By.XPATH, '//span[text()="毎日クリック"]')
    element.click()
    time.sleep(1)

    # クリックポイントを探してクリック
    elements = driver.find_elements(By.CSS_SELECTOR, ".go_btn")
    text = "クリックで1pt"

    for i, element in enumerate(elements):
        if element.text == text:
            print(f"{i}番目: {element.text}")
            element.click()
            time.sleep(2)

    driver.quit()
