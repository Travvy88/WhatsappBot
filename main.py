from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from mutagen.mp3 import MP3
import pyautogui
import os

target = ''
steps = dict()
name_att = 'UNKNOWN'


def getname():
        tt = driver.find_element_by_xpath('//span[@class = "_19RFN _1ovWX _F7Vk"]')
        return tt.get_attribute('title')


def send_msg(msg, step=0):
    global name_att
    # driver.find_element_by_class_name('_3u328').send_keys(msg)
    driver.find_element_by_xpath("//div[@class = '_2i7Ej _14Mgc copyable-area']"
                                 "/descendant::div[@class = '_3u328 copyable-text selectable-text']").send_keys(msg)   # Вставить текст в поле ввода
    driver.find_element_by_class_name('_3M-N-').click()  # Нажать на кнопку отправить
    if step:
        print(datetime.now().strftime("%x || %H:%M:%S ||"), name_att, 'STEP', step)
    else:
        print(datetime.now().strftime("%x || %H:%M:%S ||"), 'Message:', msg, '|| was sent to', name_att)


def choose(name):
    driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)).click()  # Поиск имени в контактах


def check_clck_new_msg():
    while 1:
        for i in range(1, 21):
            sleep(0.5)
            path = "//div[@class = 'X7YrQ'][{}]/" \
                   "descendant::span[@class= 'P6z4j']/" \
                   "ancestor::div[@class = 'xD91K']/" \
                   "preceding-sibling::div[@class = 'KgevS']/" \
                   "descendant::span[@class = '_19RFN _1ovWX _F7Vk']"
            # просматривает все окошки и находит те, в которых новые мсдж
            path = path.format(i)
            try:
                t = driver.find_element_by_xpath(path)
            except:
                a = 1
            else:
                name = t.get_attribute("title")  # находит имя написавшего
                if not(name in ignore_list):
                    t.click()
                    return name  # если имени нет в игнор-листе - функция завершается и возвращает имя написавшего


def click_new_msg():
    global target, name_att
    try:
        target = driver.find_element_by_xpath("//span[@class= 'P6z4j']")  # Ищет значок новых сообщений
        """
        тут функция должна прочитать имя написавшего, и если оно совпадает с игнор-листом, return 0
        причем нужно сделать так, чтобы она перешла к следующему значку новых сообщений, и так проверяла их все,
        пока не найдется, кому ответить 
        
        """
        target = driver.find_element_by_xpath("//span[@class='P6z4j']/ancestor::div[@class='X7YrQ']")
        target.click()
        name_att = getname()
        return name_att
    except:
        return 0


def plus_step(name):
    global steps
    steps[name] += 1
    print(steps)


def send_nudes(path, step=0):
    global target, wait, name_att
    target = driver.find_element_by_xpath("//div[@title = 'Приложить']").click()
    target = driver.find_element_by_xpath("//input[@type = 'file']").send_keys(path)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon = 'send-light']")))
    target = driver.find_element_by_xpath("//span[@data-icon = 'send-light']").click()
    if step:
        print(datetime.now().strftime("%x || %H:%M:%S ||"), name_att, 'STEP', step)
    else:
        print(datetime.now().strftime("%x || %H:%M:%S ||"), path, '|| nudes was sent to', name_att)


def send_voice(voice, step=0):
    global target, name_att
    v = MP3(voice)
    xy = driver.find_element_by_class_name('hjJpn').location
    wsize = driver.get_window_rect()
    os.system(voice)
    driver.find_element_by_class_name('hjJpn').click()
    sleep(v.info.length)
    pyautogui.click(wsize['x'] + xy['x'], wsize['y'] + xy['y'] + 120)
    if step:
        print(datetime.now().strftime("%x || %H:%M:%S ||"), name_att, 'STEP', step)
    else:
        print(datetime.now().strftime("%x || %H:%M:%S ||"), voice, '|| voice was sent to', name_att)


def read_last_msg():
    driver.find_element_by_xpath("//div[@class = 'FTBzM message-in']")   # в разработке


def script_test(step):
    if step == 1:
        send_msg('Сообщение 1', step)
    elif step == 2:
        send_msg('Сообщение 2', step)
    elif step == 3:
        ignore_list.append(name_att)


def script(step):
    if step == 1:
        send_msg('Привет) Как тебя зовут?', step)
    elif step == 2:
        p = "C:/Users/Travvy/Desktop/Business/Фото Вариант 1/баба 2/015-spaces.im.jpg"
        send_msg('А я Маша)', step)
        send_nudes(os.path.normpath(p), step)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "hjJpn")))
        sleep(2)
        send_msg('Че делаешь?', step)
    elif step == 3:
        p = "C:/Users/Travvy/Desktop/Business/5 Паков - Женские Голосовые сообщения/3Третий пак [noname2 - 103]/84.Я только из душа вышла.mp3"
        send_voice(os.path.normpath(p), step)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "hjJpn")))
        sleep(2)
        send_msg("Хочешь, фотки покидаю?", step)
    elif step == 4:
        p = "C:/Users/Travvy/Desktop/Business/Фото Вариант 1/баба 2/r5ew-spaces.im.jpg"
        p1 = "C:/Users/Travvy/Desktop/Business/Фото Вариант 1/баба 2/354-spaces.im.jpg"
        send_nudes(os.path.normpath(p), step)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "hjJpn")))
        sleep(2)
        send_nudes(os.path.normpath(p1), step)
    elif step == 5:
        send_msg('Ghfdlf&', step)
        send_msg('Правда?', step)
    elif step == 6:
        p = "C:/Users/Travvy/Desktop/Business/Фото Вариант 1/баба 2/65467-spaces.im.jpg"
        p1 = "C:/Users/Travvy/Desktop/Business/Фото Вариант 1/баба 2/65-spaces.im (1).jpg"
        send_nudes(os.path.normpath(p), step)
        sleep(2)
        send_nudes(os.path.normpath(p1), step)
        sleep(2)
        send_msg('А покидай свои фотки))', step)
    elif step == 7:
        ignore_list.append(name_att)


options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_mic": 1})

driver = webdriver.Chrome(options=options)
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 500)
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "_3H4MS")))

voice = 'C:/Users/Travvy/Desktop/WhatsappTest/ясно.mp3'
teaser = 'C:/Users/Travvy/Desktop/WhatsappTest/тизер.mp4'
serg = "C:/Users/Travvy/Desktop/МИЭМс/qhysq_AVrX4.jpg"

message = 'Отныне бот отправляет мем, видос и голосовуху. Спасибо за внимание.'
t = 5  # период проверки на новые сообщения

'''
choose(default)  # click default
while 1 == 1:
    if click_new_msg() != 0:
        send_msg(message)
        sleep(2)  # прописать wait операторы в функции
        send_nudes(serg)
        sleep(2)
        send_nudes(teaser)
        sleep(2)
        send_voice(voice)
        name_att = 'UNKNOWN'
    else:
        print(datetime.now().strftime("%x || %H:%M:%S ||"), 'No new messages')
        choose(default)  # click default
        sleep(t)

ignore_list = ['']
default = '+7 925 596-54-02'
choose(default)  # click default
while 1 == 1:
    name_att = 'UNKNOWN'
    if click_new_msg() != 0:
        name = getname()
        if not(name in ignore_list):
            if name in steps:
                steps[name] += 1
            else:
                steps[name] = 1
            script(steps[name])
            choose(default)
    else:
        print(datetime.now().strftime("%x || %H:%M:%S ||"), 'No new messages')
        choose(default)  # click default
        sleep(t)
'''
ignore_list = ['Саша Ладовир']
default = 'Бабушка'
choose(default)  # click default
name_att = 'UNKNOWN'

while 1:
    name_att = check_clck_new_msg()
    if name_att in steps:
        steps[name_att] += 1
    else:
        steps[name_att] = 1
    script_test(steps[name_att])
    choose(default)  # click default





