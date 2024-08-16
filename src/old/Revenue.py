import time

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.airdna.co/vacation-rental-data/app/us/california/santa-monica/revenue")
driver.find_element_by_xpath("//button[text()='Log In']").click()
driver.find_element_by_id("login-email").send_keys("stays.atithi@gmail.com")
driver.find_element_by_id("login-password").send_keys("Atithi2021stays$")
driver.find_element_by_class_name("custom-modal__submit-button").click()

while True:
    input("Press Enter to continue...")

    # elements = driver.find_element_by_xpath("//div[@class ='percentile-filter']/button[3]")
    # elements.click()

    one = driver.find_element_by_class_name("chart__dot")
    elements = driver.find_elements_by_class_name("chart__dot")
    target_list = []

    for i in range(13):
        elements[i].click()
        html = driver.page_source

        soup = BeautifulSoup(html, "lxml")

        values = soup.find_all("p", {"class": ['gltyAz']})

        for value in values:
            target_list.append(value.text)

        output = ' , '.join(target_list)
    print(output)
    occupancy = output.replace('$', '').split(' ,')
    total = 0
    for num in occupancy:
        total += int(num.replace(',', ''))
    total /= 13
    print(total)

    
driver.quit()
NightlyRate.py