import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

nav = webdriver.Chrome()

nav.get('https://wcaquino.me/cypress/componentes.html')
nav.find_element('id', 'buttonSimple').click()
nav.find_element('id', 'buttonLazy').click()
nav.find_element('id', 'buttonCount').click()
nav.find_element('id', 'buttonList').click()
nav.find_element('id', 'buttonListDOM').click()
#nav.find_element('id', 'buttonPopUp').click()
nav.find_element('id', 'buttonDelay').click()
nav.find_element('id', 'buttonNow').click()
nav.find_element('id', 'buttonTimePassed').click()
nav.find_element('id', 'formNome').send_keys('Pedro Pedro')
nav.find_element('id', 'formSobrenome').send_keys('Pedro Pedro')
nav.find_element('id', 'formSexoMasc').click()
nav.find_element('id', 'formComidaCarne').click()
nav.find_element('id', 'formComidaFrango').click()
nav.find_element('id', 'formComidaPizza').click()
#nav.find_element('id', 'formComidaVegetariana').click()
y = nav.find_element('id', 'formEscolaridade')
down = Select(y)
down.select_by_visible_text('2o grau completo')
x = nav.find_element('id', 'formEsportes')
drop = Select(x)
drop.select_by_visible_text('Natacao')
nav.find_element('id', 'elementosForm:sugestoes').send_keys('dadsaasdsadasdasdasfsadfgasdgagagqaregergerger')
nav.find_element('xpath', '//*[@id="tabelaUsuarios"]/tbody/tr[1]/td[4]/input').click()
nav.find_element('xpath', '//*[@id="tabelaUsuarios"]/tbody/tr[2]/td[4]/input').click()
nav.find_element('xpath', '//*[@id="tabelaUsuarios"]/tbody/tr[3]/td[4]/input').click()
nav.find_element('xpath', '//*[@id="tabelaUsuarios"]/tbody/tr[4]/td[4]/input').click()
nav.find_element('xpath', '//*[@id="tabelaUsuarios"]/tbody/tr[5]/td[4]/input').click()
nav.find_element('xpath', '//*[@id="tabelaUsuarios"]/tbody/tr[1]/td[5]/table/tbody/tr/td/input').click()
nav.find_element('xpath', '//*[@id="tabelaUsuarios"]/tbody/tr[2]/td[5]/table/tbody/tr/td/input').click()
nav.find_element('xpath', '//*[@id="tabelaUsuarios"]/tbody/tr[3]/td[5]/table/tbody/tr/td/input').click()
nav.find_element('xpath', '//*[@id="tabelaUsuarios"]/tbody/tr[4]/td[5]/table/tbody/tr/td/input').click()
nav.find_element('xpath', '//*[@id="tabelaUsuarios"]/tbody/tr[5]/td[5]/table/tbody/tr/td/input').click()
nav.find_element('xpath', '//*[@id="tabelaUsuarios"]/tbody/tr[1]/td[6]/input').send_keys('Pedro')
nav.find_element('xpath', '//*[@id="tabelaUsuarios"]/tbody/tr[2]/td[6]/input').send_keys('Pedro')
nav.find_element('xpath', '//*[@id="tabelaUsuarios"]/tbody/tr[3]/td[6]/input').send_keys('Pedro')
nav.find_element('xpath', '//*[@id="tabelaUsuarios"]/tbody/tr[4]/td[6]/input').send_keys('Pedro')
nav.find_element('xpath', '//*[@id="tabelaUsuarios"]/tbody/tr[5]/td[6]/input').send_keys('Pedro')
nav.find_element('id', 'formCadastrar').click()