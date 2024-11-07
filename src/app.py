from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl

driver = webdriver.Chrome()
driver.get('https://www.idealista.pt/comprar-casas/lisboa/')

titles = driver.find_elements(By.XPATH, "//a[@class='item-link ']")
prices = driver.find_elements(By.XPATH, "//span[@class='item-price h2-simulated']")

# for test purpose 
for title in titles: 
    print(title.text)

for price in prices:
    print(price.text)

try:
    buttons = driver.find_elements(By.XPATH, "//button[@class='icon-phone hidden-contact-phones_link see-phones-btn fake-anchor']")

    for button in buttons:
        ActionChains(driver).move_to_element(button).click(button).perform()

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='hidden-contact-phones_text']"))
        )

    numbers = driver.find_elements(By.XPATH, "//span[@class='hidden-contact-phones_text']")

    for number in numbers:
        print(number.text)

finally:
    driver.quit()

workbook = openpyxl.Workbook()
workbook.create_sheet('housesIdealista')
sheet_houses = workbook['housesIdealista']

sheet_houses['A1'].value = 'Descrição'
sheet_houses['B1'].value = 'Preço'
sheet_houses['C1'].value = 'Telefone'



