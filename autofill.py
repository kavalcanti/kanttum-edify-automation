from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

#init webdriver
url_form = grades[0]

driver = webdriver.Firefox()
driver.get(url_form)
WebDriverWait(driver,10).until(presence_of_element_located((By.NAME,"identifier")))

#login
driver.find_element_by_name('identifier').send_keys(email_mentor)
driver.find_element_by_name('identifier').send_keys(Keys.RETURN)
WebDriverWait(driver,10).until(presence_of_element_located((By.NAME,"password")))
driver.find_element_by_name('password').send_keys(senha_mentor)
driver.find_element_by_name('password').send_keys(Keys.RETURN)
WebDriverWait(driver,20).until(presence_of_element_located((By.CLASS_NAME,"header-title")))

#expandir criterios
crits = driver.find_elements_by_class_name("header-title")
for crit in crits:
    crit.click()
    driver.implicitly_wait(0.2)
    
#lançar notas
nao_aplicavel = driver.find_elements_by_xpath("//*[text() = 'Não aplicável']")
not_evident = driver.find_elements_by_xpath("//*[text() = 'Not Evident']")
fairly_evident = driver.find_elements_by_xpath("//*[text() = 'Fairly Evident']")
evident = driver.find_elements_by_xpath("//*[text() = 'Evident']")
very_evident = driver.find_elements_by_xpath("//*[text() = 'Very Evident']")

for i, grade in enumerate(grades):
    if grade == 'Very Evident':
        very_evident[i].click()
        driver.implicitly_wait(0.2)
    elif grade == 'Evident':
        evident[i].click()
        driver.implicitly_wait(0.2)
    elif grade == 'Fairly Evident':
        fairly_evident[i].click()
        driver.implicitly_wait(0.2)
    elif grade == 'Not Evident':
        not_evident[i].click()
        driver.implicitly_wait(0.2)
    elif grade == 'Não aplicável':
        nao_aplicavel[i].click()
        driver.implicitly_wait(0.2)
    else:
        nao_aplicavel[i].click()
        driver.implicitly_wait(0.2)
