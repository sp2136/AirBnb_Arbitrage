import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.airdna.co/vacation-rental-data/app/us/california/santa-monica/occupancy")
while True:

    driver.find_element(By.XPATH, "//button[text()='Log In']").click()

    driver.find_element(By.ID, "login-email").send_keys("stays.atithi@gmail.com")
    driver.find_element(By.ID, "login-password").send_keys("Atithi2021stays$")

    driver.find_element(By.CLASS_NAME, "custom-modal__submit-button").click()
    input("Press Enter to continue...")

    # elements = driver.find_element_by_xpath("//div[@class ='percentile-filter']/button[3]")
    # elements.click()

    one = driver.find_element(By.CLASS_NAME, "chart__dot")
    elements = driver.find_elements(By.CLASS_NAME, "chart__dot")
    target_list = []
    target_list2 = []

    for i in range(22, 34):
        elements[i].click()
        html = driver.page_source

        soup = BeautifulSoup(html, "lxml")

        values = soup.find_all("p", {"class": ['gltyAz']})
        values2 = soup.find_all("p", {"class": ['bwRIJU']})

        for value in values:
            target_list.append(value.text)
        for value in values2:
            target_list2.append(value.text)

        output = ' , '.join(target_list)
        output2 = ' , '.join(target_list2)

    print(output)
    print(output2)

    occupancy = output.replace('%', '').split(',')
    occupancy2 = output2.replace('%', '').split(',')
    total = 0
    for num in occupancy:
        total += int(num)
    total /= 12
    print("50th" + str(total))

    total = 0
    for num in occupancy2:
       total += int(num)
    total /= 12
    print("75th" + str(total))

driver.quit()
NightlyRate.py

driver.quit()
