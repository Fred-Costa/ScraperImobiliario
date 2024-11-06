import openpyxl.workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
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

phoneNumber = driver.find_elements(By.XPATH, "//span[@class='item-price h2-simulated']")

# for test purpose
""" for price in prices:
    print(price.text) """


workbook = openpyxl.workbook()
workbook.create_sheet('housesIdealista')
sheet_houses = workbook['housesIdealista']

sheet_houses['A1'].value = 'Descrição'
sheet_houses['B1'].value = 'Preço'
sheet_houses['C1'].value = 'Telefone'



