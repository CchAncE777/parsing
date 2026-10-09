from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome()

driver.get('https://lessons.zennolab.com/ru/registration')

wait = WebDriverWait(driver, 10)

email_input = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
email_input.clear()
email_input.send_keys("lol@hello")

password_input = wait.until(EC.element_to_be_clickable((By.ID, 'password')))
password_input.clear()
password_input.send_keys("123456")

password_confirm_input = wait.until(EC.element_to_be_clickable((By.ID, 'password_repeat')))
password_confirm_input.clear()
password_confirm_input.send_keys("123456")

submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Создать аккаунт"]')))
submit_button.click()

print("Текст успешно введен в поле!")
time.sleep(5)