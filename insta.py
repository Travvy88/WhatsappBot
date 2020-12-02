from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 500)


def authorize(login, password):
    driver.get('https://www.instagram.com')
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name = 'username']")))
    pole_login = driver.find_element_by_xpath("//input[@name = 'username']")
    pole_login.send_keys(login)
    pole_password = driver.find_element_by_xpath("//input[@type = 'password' ]")
    pole_password.send_keys(password)
    button = driver.find_element_by_xpath("//button[@type ='submit']")
    button.click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/section/div/button')))


def count_stories(account):
    sleep(2)
    driver.get('https://www.instagram.com/' + account)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//canvas[@class = "CfWVH"]')))
    circle = driver.find_element_by_xpath('//img[@class = "_6q-tv"]')
    circle.click()
    sleep(2)
    stories = driver.find_elements_by_xpath('//div[@class = "_7zQEa"]')
    return len(stories)


if __name__ == "__main__":
    login = 'travvy.jb'
    password = 'YoungTravvyInstagram88'
    acc = '4chan_tv'

    authorize(login, password)
    print(count_stories(acc))