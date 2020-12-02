import pyautogui
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

target = input('Target: ')
msg = input('Message: ')

target = driver.find_element_by_xpath('//span[@title = "{}"]'.format(target))
target.click()
sleep(2)
pyautogui.moveTo(599, 984)
pyautogui.click(button = 'left')
sleep(2)
pyautogui.write('rgttr')

