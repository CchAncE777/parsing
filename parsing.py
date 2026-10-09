from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium import webdriver

driver= webdriver.Chrome()

driver.get("https://catalog.onliner.by/mobile")

# Собираем все ссылки на объявления с выбранной страницы
def get_all_links_on_page():
    elements = driver.find_elements(By.CLASS_NAME, value='catalog-form__link')
    # elements = driver.find_elements(by=By.CSS_SELECTOR, value="#container > div > div > div > div > div.catalog-content > div.catalog-wrapper > div > div > div.catalog-form__tabs > div > div > div > div > div.catalog-form__filter-part.catalog-form__filter-part_2 > div.catalog-form__offers > div > div:nth-child(1) > div > div > div.catalog-form__offers-part.catalog-form__offers-part_data > div.catalog-form__description.catalog-form__description_primary.catalog-form__description_base-additional.catalog-form__description_font-weight_semibold.catalog-form__description_condensed-other > a")
    # <a href="https://catalog.onliner.by/mobile/xiaomi/redmi15c8256ebk" class="catalog-form__link catalog-form__link_primary-additional catalog-form__link_base-additional catalog-form__link_font-weight_semibold catalog-form__link_nodecor"> Телефон Xiaomi Redmi 15C 4G 8GB/256GB международная версия (черный) </a>
    ads_list = []
    for element in elements:
        ads_list.append(element.get_attribute('href'))
        # print(element.get_attribute('href'), '\n')

    return ads_list

def click_next_page():
    clickable_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[4]/div/div/div/div/div[3]/div[3]/a'))
    )

    clickable_element.click()

def clean_links(links: list):
    print(f'Start size of links list: {len(links)}')
    clear_links = []
    very_clear_links = []

    for item in links:
        if item == None or 'forum.' in item or 'tech.' in item:
            pass
        else:
            clear_links.append(item)
    print(f'Current size of links list: {len(clear_links)}')

    for item in clear_links:
        if 'prices' in item or 'reviews' in item or 'used' in item:
            pass
        else:
            very_clear_links.append(item)
    print(f'Finish size of links list: {len(very_clear_links)}')

    return very_clear_links

links_list = []
try:
    for iter in range(0, 5, 1):
        links_list += get_all_links_on_page()
        click_next_page()
except:
    print("All done")
    clean_links_list = clean_links(links_list)
finally:
    print("All done")
    clean_links_list = clean_links(links_list)

def get_characteristics():
    character_dict = {}
    character_dict.update({'Название модели': driver.find_element(By.CLASS_NAME, value='catalog-masthead__title').text})
    elements = driver.find_elements(By.CSS_SELECTOR, value='.product-specs__table tr')
    for item in elements: 
        tds = item.find_elements(By.TAG_NAME, value='td')
        if len(tds) == 2:
            if not tds[1].text:
                if tds[1].find_elements(By.CLASS_NAME, value='i-x'):
                    character_dict.update({tds[0].text: 'No'})
                else:
                    character_dict.update({tds[0].text: 'Yes'})
            else:
                character_dict.update({tds[0].text:tds[1].text})
    
    for key,value in character_dict.items():
        print(f'{key}: {value}')  

    return character_dict   

table = pd.DataFrame()
for link in clean_links_list[0:10]:
    driver.get(link)
    
    new_row = pd.DataFrame([get_characteristics()])
    table = pd.concat([table , new_row] , ignore_index=True)
    



import csv

model_row.keys()

table = pd.DataFrame([model_row])
table

characteristics_table = pd.DataFrame(columns=model_row.keys())
characteristics_table
characteristics_table = pd.concat([characteristics_table, pd.DataFrame(model_row)], axis=1)
characteristics_table