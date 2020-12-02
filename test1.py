
from selenium import webdriver

rome()
driver.get('https://web.whatsapp.com/')

name = input('Target: ')
msg = input('Message: ')
count = int(input('Count: '))

input('Enter anything after scanning QR code ')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_3u328')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()