from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from settings import maill, password, test
from bs4 import BeautifulSoup
import requests


driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")


try:
    # Загружаем страницу
    driver.get("https://roo-nag.educhel.ru")

    # Подтверждаем вывод модального окна cukies через явное ожидание...
    cukies = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']")))
    
    # Кликаем "ok" в  модальном окне cukies
    cukies.click()

    # Подтверждаем кликабельность ссылки в ЛК Администратора через явное ожидание...
    url_admin = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Вход для администратора']")))

    # Кликаем по ссылке Вход для администратора
    url_admin.click()

    # Подтверждаем вывод формы ввода email через явное ожидание...
    email_form = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='loginform-email']")))

    # Отчищаем форму ввода email_form
    email_form.clear()

    # Вводим почту администратора
    email_form.send_keys(maill)

    # Подтверждаем вывод формы ввода passw через явное ожидание...
    passw_form = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='loginform-password']")))

    # Отчищаем форму ввода passw_form
    passw_form.clear()

    # Вводим пароль администратора
    passw_form.send_keys(password)

    # Подтверждаем кликабельность кнопки "ввод" для подтверждения введенных данных администратора через явное ожидание
    input_btn = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.btn")))

    # Кликаем по кнопке "Ввод"
    input_btn.click()

    # Подтверждаем кликабельность url для перехода в раздел  "Управление" через явное ожидание...
    url_razd_upr = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Управление        ']")))

    # Кликаем по ссылке "Управление"
    url_razd_upr.click()

    # Подтверждаем кликабельность url для перехода в подраздел  "Новости Управления образования" через явное ожидание...
    url_news_upr = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Новости Управления образования']")))

    # Кликаем по ссылке "Новости Управления образования"
    url_news_upr.click()

    # Подтверждаем кликабельность url для перехода в раздел  "Редактирование" через явное ожидание...
    settings_url = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Редактировать']")))

    # Кликаем по ссылке "Редактирование"
    settings_url.click()

    # Подтверждаем кликабельность url для перехода в раздел  "Добавить новость" через явное ожидание...
    url_add_news = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='navbar-collapse']/ul/li[1]/a")))

    # Кликаем по кнопке "Добавить новость"
    url_add_news.click()
    time.sleep(10)

    # Блок парсер...
    # Создаем заголовок для отправки серверу...
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

    # Загружаем HTML-страницу с помощью библиотеки requests
    url = "https://roo-nag.educhel.ru/government/news"
    response = requests.get(url, headers=headers)
    html = response.content

    # Инициализируем объект BeautifulSoup для парсинга HTML-кода
    soup = BeautifulSoup(html, 'html.parser')

    # Находим все блоки div вложенные в блок div c классом "eip-sortable-news news-masonry row"
    divs = soup.find_all("div", class_="eip-sortable-news news-masonry row")

    # Инициализируем переменную для хранения наибольшего значения id
    max_id = None

    # Проходимся по всем блокам div и ищем максимальное значение id
    for div in divs:
        div_id = div.get('id')
        if div_id is not None and (max_id is None or int(div_id) > int(max_id)):
            max_id = div_id



    # Выводим наибольшее значение id на экран
    print("Наибольший по значению id блок div: ", max_id)



    # Подтверждаем кликабельность url для выхода из в режима редактирования...
    url_add_news = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{test}']"))).click
    time.sleep(5)






    '''''
    # Вводим название статьи...
    title_news = driver.find_element(By.CSS_SELECTOR, "div[data-widget-id='w2']>div")
    title_news.clear()
    title_news.send_keys(content_title_news)
    
    # Вводим дату публикции статьи...
    if content_date_news == 'none':
        date_news = driver.find_element(By.CSS_SELECTOR, "div[data-widget-id='w3']>input")
        date_news.clear()
        date_news.send_keys(tec_date)
    else:
        date_news = driver.find_element(By.CSS_SELECTOR, "div[data-widget-id='w3']>input")
        date_news.clear()
        date_news.send_keys(content_date_news)
     

    # Вводим описание статьи...
    desc_news = driver.find_element(By.CSS_SELECTOR, "div[data-widget-id='w4']>div")
    desc_news.clear()
    desc_news.send_keys(content_desc_news)

    # Подтверждаем кликабельность url для выхода из в режима редактирования...
    url_add_news = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Выйти']"))).click
    time.sleep(5)

    '''''


finally:
    # Прекращаем работу драйвера...
    driver.close()
    print(divs)

    # выводим сообщение в консоль...
    print("Тест пройден успешно!!!")

    





