from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from settings import maill, password, content_title, content_desc, tec_date

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

    # Кликаем по ссылке "Добавить новость"
    url_add_news.click()

    # Объявляем функцию обработки текущий даты для размещения новостей....

    def is_price_correct(driver, tec_date):
        price_locator = (By.XPATH, '//input[@value="29.12.2022"] and contains(@input, "'+tec_date+'")]')

        return is_price_correct(driver, tec_date)






    # Отчищаем форму ввода news_carousel_header
    # news_carousel_header.clear()


    # Вводим Заголовок статьи
    # news_carousel_header.send_keys(content_title)

    # Подтверждаем вывод формы ввода news_carousel_desc через явное ожидание...
    # news_carousel_desc = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='_api_eip_edit_EdudepPost_short']")))

    # Отчищаем форму ввода news_carousel_desc
    # news_carousel_desc.clear()

    # Вводим Краткое описание статьи
    # news_carousel_desc.send_keys(content_desc)

    # Подтверждаем кликабельность url Сохранить через явное ожидание...
    # url_save_news = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Сохранить']")))

    # Кликаем по ссылке "Сохранить"
    # url_save_news.click()

    # Подтверждаем кликабельность url Продолжить чтение через явное ожидание...
    # url_redactor_news = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='3147820']/article/a")))

    # Кликаем по ссылке "Продолжить чтение"
    # url_redactor_news.click()

    # Засыпаем на 3 секунды
    time.sleep(3)


finally:
    driver.close()                       # Прекращаем работу драйвера...
    print("Тест пройден успешно!!!")     # выводим сообщение в консоль...
    print(tec_date)                      # Выводим текущую дату
    





