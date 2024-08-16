import time

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.airdna.co/vacation-rental-data/app/us/california/santa-monica/occupancy")
while True:
    input("Press Enter to continue...")

    # elements = driver.find_element_by_xpath("//div[@class ='percentile-filter']/button[3]")
    # elements.click()
    search = driver.find_element_by_class_name("location-bar__region-select")
    search.click()
    search = driver.find_element_by_class_name("css-s67jrt-menu")
    search.click()
    # one = driver.find_element_by_class_name("chart__dot")
    # elements = driver.find_elements_by_class_name("chart__dot")
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
    output = output.replace('%', '').split(',')
    total = 0
    for num in output:
        total += int(num)
    total /= 13
    print(total)
driver.quit()
