import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
# 4246315344375660

driver = webdriver.Chrome()
driver.get("https://www.zillow.com/b/617-w-fulton-st-chicago-il-9S6x2m/")
# driver.get("https://www.airdna.co/vacation-rental-data/app/us/california/santa-monica/rates")


for num in range(000, 999):
    input("Press Enter to continue...")
    # cvv = driver.find_element(By.ID, "verificationCode")
    btn = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/p']")
    # cvv.clear()
    # cvv.send_keys(str(num).zfill(3))
    # btn.click()
    print(num)
    input("Press Enter to continue...")

driver.quit()

