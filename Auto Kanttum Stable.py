#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

def converter_notas(nota):
    if nota == '3':
        mencao = 'Very Evident'
    elif nota == '2':
        mencao = 'Evident'
    elif nota == '1':
        mencao = 'Fairly Evident'
    elif nota == '0':
        mencao = 'Not Evident'
    elif nota == '':
        mencao = 'Não aplicável'
    else:
        mencao = nota
    return mencao

grades = []
criteria_str = ['Form URL:',
           'Crit 1',
           'Crit 2',
           'Crit 3',
           'Crit 4',
           'Crit 5',
           'Crit 6',
           'Crit 7',
           'Crit 8',
           'Crit 9',
           'Crit 10',
           'Crit 11',
           'Crit 12',
           'Crit 13',
           'Crit 14',
           'Crit 15',
           'Crit 16',
           'Crit 17',
           'Crit 18',
           'Crit 19',
           'Crit 20',
           'Crit 21',
           'Crit 22',
           'Crit 23',
           'Crit 24',
           'Crit 25',
           'Crit 26',
           'Crit 27']

#dados de login
email_mentor = input('E-mail cadastrado: ')
senha_mentor = input('Senha: ')
#coleta das notas.
print('Hit ENTER for Not Applicable.')
for criterion in criteria_str:
    add = input('{}'.format(criterion))
    grades.append(converter_notas(add))

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

