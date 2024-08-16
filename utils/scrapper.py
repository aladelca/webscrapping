from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.utils import prepare_name
import time
import numpy as np
import warnings
warnings.filterwarnings('ignore')  

def get_scrapped_data(text):
    text = prepare_name(text)
    print('Start of scrapping')
    url = f'https://www.falabella.com.pe/falabella-pe/search?Ntt={text}'
    driver_path = '/opt/homebrew/bin/chromedriver'
    service = Service(executable_path = driver_path)
    driver = webdriver.Chrome(service = service)
    driver.get(url)
    driver.maximize_window()
    titles = []
    sellers = []
    offer_prices = []
    regular_prices = []
    catalog_prices = []
    brands = []
    images = []
    try:
        all_pages = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/section[2]/div[1]/div[1]/div/div[2]/div/ol/li[5]/button')
        all_pages = int(all_pages.text)
    except:
        all_pages = 100
    try:
        total = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/section[2]/div[1]/div[4]/div[1]/div/span/span')
        total_number = int(total.text[total.text.find('-')+2:total.text.find('de')].strip())+1
    except:
        total_number = 48
    for page in range(1,all_pages+1):
        y = 1500
        for i in range(1,total_number):
            try:
                title = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[2]/div[2]/section[2]/div[1]/div[3]/div[{i}]/a/div[2]/div[1]/b')                                    
                titles.append(title.text)
                print(title.text)
            except:
                try:
                    title = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[2]/div[3]/section[2]/div[1]/div[3]/div[{i}]/a/div[2]/div[1]/b')
                    titles.append(title.text)
                    print(title.text)
                except:
                    title = np.nan
                    titles.append(title)
                    pass
            try:
                seller = driver.find_element(By.XPATH,  f'/html/body/div/div/div[2]/div[2]/section[2]/div[1]/div[3]/div[{i}]/a/div[2]/div[1]/span/b')
                sellers.append(seller.text)
                print(seller.text)  
            except:
                seller = np.nan
                sellers.append(seller)
                print(seller)
            try:
                offer_price = driver.find_element(By.XPATH,  f'/html/body/div[1]/div/div[2]/div[2]/section[2]/div[1]/div[3]/div[{i}]/a/div[3]/div[1]/ol/li[1]/div/span')                                 
                offer_prices.append(offer_price.text)
                print(offer_price.text)
            except:
                try:
                    offer_price = driver.find_element(By.XPATH,  f'/html/body/div[1]/div/div[2]/div[3]/section[2]/div[1]/div[3]/div[{i}]/a/div[3]/div[1]/ol/li[1]/div/span')
                    offer_prices.append(offer_price.text)
                    print(offer_price.text)
                except:
                    offer_price = np.nan
                    offer_prices.append(offer_price)
                    print(offer_price)
            try:
                regular_price = driver.find_element(By.XPATH,  f'/html/body/div[1]/div/div[2]/div[2]/section[2]/div[1]/div[3]/div[{i}]/a/div[3]/div[1]/ol/li[2]/div/span')
                                                                
                regular_prices.append(regular_price.text)
                print(regular_price.text)
            except:
                try:
                    regular_price = driver.find_element(By.XPATH,  f'/html/body/div[1]/div/div[2]/div[3]/section[2]/div[1]/div[3]/div[{i}]/a/div[3]/div[1]/ol/li[2]/div/span')
                    regular_prices.append(regular_price.text)
                    print(regular_price.text)
                except:
                    regular_price = np.nan
                    regular_prices.append(regular_price)
                    print(regular_price)
            try:
                catalog_price = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[2]/div[2]/section[2]/div[1]/div[3]/div[{i}]/a/div[3]/div[1]/ol/li[3]/div/span')                                                                                                    
                catalog_prices.append(catalog_price.text)
                print(catalog_price.text)
            except:
                try:
                    catalog_price = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[2]/div[3]/section[2]/div[1]/div[3]/div[{i}]/a/div[3]/div[1]/ol/li[3]/div/span')
                    catalog_prices.append(catalog_price.text)
                    print(catalog_price.text)
                except:
                    catalog_price = np.nan
                    catalog_prices.append(catalog_price)
                    print(catalog_price)
            try:
                brand = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[2]/div[2]/section[2]/div[1]/div[3]/div[{i}]/a/div[2]/div[1]/div/b')                
                brands.append(brand.text)
                print(brand.text)
            except:
                try:
                    brand = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[2]/div[3]/section[2]/div[1]/div[3]/div[{i}]/a/div[2]/div[1]/div/b')
                    brands.append(brand.text)
                    print(brand.text)   
                except:
                    brand = np.nan
                    brands.append(brand)
                    print(brand)
            if i%8 == 0:   
                time.sleep(10)
                
                driver.execute_script(f"window.scrollTo(0, {y})")
                y = y + 1200

            try:
                img = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[2]/div[2]/section[2]/div[1]/div[3]/div[{i}]/a/div[1]/div[1]/section/picture[1]/img')                                      
                img_url = img.get_attribute('src')
                images.append(img_url)
                print(img_url)
            except:
                try:
                    img = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[2]/div[3]/section[2]/div[1]/div[3]/div[{i}]/a/div[1]/div[1]/section/picture[1]/img')
                    img_url = img.get_attribute('src')
                    images.append(img_url)
                    print(img_url)
                except:     
                    img = np.nan
                    images.append(img)
                    print(img)

        driver.execute_script(f"window.scrollTo(0, 0)")
        try:
            next_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/section[2]/div[1]/div[1]/div/div[2]/div/div[2]/button')
        #next_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/section[2]/div[1]/div[4]/div[2]/div[2]/button')
            next_button.click()
        except:
            try:
                next_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/section[2]/div[1]/div[1]/div/div[2]/div/div[2]/button')
                next_button.click()
            except: 
                pass
    print('End of scrapping')
    print(f'Data scrapped: {len(titles)}')
    if len(titles) == len(sellers) == len(offer_prices) == len(regular_prices) == len(catalog_prices) == len(brands) == len(images):

        return titles, sellers, offer_prices, regular_prices, catalog_prices, brands, images
    else:
        return titles, sellers[:len(titles)], offer_prices[:len(titles)], regular_prices[:len(titles)], catalog_prices[:len(titles)], brands[:len(titles)], images[:len(titles)]