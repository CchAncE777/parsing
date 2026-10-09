from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()

driver.get("https://lessons.zennolab.com/captchas/recaptcha/v2_simple.php?level=low")

iframe = driver.find_element(By.XPATH, "//iframe[contains(@name, 'a-')]")
driver.switch_to.frame(iframe)
sitekey = driver.find_element(By.ID, "recaptcha-token").get_attribute("value")
driver.switch_to.default_content()


print(sitekey)