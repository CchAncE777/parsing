from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha
import time

driver= webdriver.Chrome()

driver.get('https://rucaptcha.com/demo/normal')

wait = WebDriverWait(driver, 10)

captcha_png = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//img[@alt="пример простой капчи"]')
        )
    )
captcha_png.screenshot('captcha.png')

API_KEY = ""
solver = TwoCaptcha(API_KEY)

result = solver.normal("captcha.png", server="rucaptcha.com")
captcha_text = result["code"]


captcha_confirm = wait.until(EC.element_to_be_clickable((By.ID, 'simple-captcha-field')))
captcha_confirm.clear()
captcha_confirm.send_keys(captcha_text)

submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-action="demo_action"]')))
submit_button.click()

print("Текст успешно введен в поле!")
time.sleep(5)
