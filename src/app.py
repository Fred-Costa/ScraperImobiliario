import openpyxl.workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import openpyxl

driver = webdriver.Chrome()
driver.get('https://www.idealista.pt/comprar-casas/lisboa/')

titles = driver.find_elements(By.XPATH, "//a[@class='item-link ']")

# for test purpose 
""" for title in titles: 
    print(title.text) """

prices = driver.find_elements(By.XPATH, "//span[@class='item-price h2-simulated']")

# for test purpose
""" for price in prices:
    print(price.text) """

try:
    buttons = driver.find_elements(By.XPATH, "//button[@class='icon-phone hidden-contact-phones_link see-phones-btn fake-anchor']")

    for button in buttons:
        ActionChains(driver).move_to_element(button).click(button).perform
        time.sleep(10)
        print(button)
        print("_________")
        print(button.text)

    numbers = driver.find_elements(By.XPATH, "//span[@class='hidden-contact-phones_text']")

    for number in numbers:
        print(number.text)

finally:

    driver.quit()

""" workbook = openpyxl.workbook()
workbook.create_sheet('housesIdealista')
sheet_houses = workbook['housesIdealista']

sheet_houses['A1'].value = 'Descrição'
sheet_houses['B1'].value = 'Preço'
sheet_houses['C1'].value = 'Telefone' """



