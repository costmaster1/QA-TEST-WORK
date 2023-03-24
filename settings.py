# import docx                                      # Импортируем библиотеку "python docx"
# import datetime                                  # Импортируем библиотеку "datetime"


'''
# Блок парсер...
# Создаем заголовок для отправки серверу...
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
response = requests.get('https://roo-nag.educhel.ru/government/news', headers=headers).text  # Парсим страничку news сайта...

# Сохраняем страницу в файл...
try:
    with open("index.html", "w", encoding='utf-8') as f:
        f.write(response)
        f.close()

    # Парсим данные библиотекой BeautifulSoup...
    with open("index.html", "r", encoding='utf-8') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, "lxml")
        print(soup.find(id="w2"))

except ValueError:
    print("error_file")


# Блок получения текущей даты...
dt = datetime.datetime.now()                     # Получаем текущую дату
tec_date = dt.strftime('%d.%m.%Y')               # Редактируем формат вывода текущий даты

'''


# Блок авторизации...
maill = "osoben1@yandex.ru"                      # Данные для авторизации модератора login
password = "Вка5248"                             # Данные для авторизации password

'''

# Блок управления контентом...
document = docx.Document('test.docx')            # Открываем тестовый документ "test.docx"

content_title_news = document.paragraphs[0].text      # Объявляем переменную для чтения 1 го параграфа
content_desc_news = document.paragraphs[1].text       # Объявляем переменную для чтения 2 го параграфа
content_news = document.paragraphs[2].text            # Объявляем переменную для чтения 3 го параграфа
content_date_news = document.paragraphs[3].text       # Объявляем переменную для чтения 4 го параграфа

'''
# Блок тестирования  переменной для локатора

test = "Выйти"




