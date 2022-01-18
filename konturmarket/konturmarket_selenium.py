import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from konturmarket.konturmarket_urls import ASSORTMENT_EGAIS_URL
from privatedata.kontrurmarket_privatedata import USER, PASSWORD

DEBUG = True  # Режим тестирования

options = webdriver.ChromeOptions()

if not DEBUG:
    # Если не тестируем, то Chrome запускаем в "безголовом" режиме.
    options.add_argument('--headless')

options.add_argument('user_agen=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/97.0.4692.71 Safari/537.36')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(ASSORTMENT_EGAIS_URL)
# переходим на вкладку входа по паролю
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/a[1]').click()
# Вход в сервис. Регистрация пользователя.
# Находим input для логина
user_name_element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/span/form/div[1]/div/span/span/label/span[2]/input')
user_name_element.clear()
# Вводим в поле логин
user_name_element.send_keys(USER)
# Находим input для пароля
password_element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/span/form/div[2]/div/span/div/label/span[2]/input')
password_element.clear()
# Вводим в поле пароль
password_element.send_keys(PASSWORD)
# Находим кнопки "Войти" и нажимаем ее
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/span/form/div[3]/div[2]/span/button').click()
# Если не выставить паузу, то следующий driver.get() не сработает
time.sleep(5)

# Переход в каталог ЕГАИС номенклатуры
# Переход в раздел Товары
driver.get(ASSORTMENT_EGAIS_URL)
time.sleep(20)
# test_element = driver.find_element(By.XPATH,
#                                        '//*[@id="root"]/div/div[3]/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div/span')

print(driver.current_url)
# time.sleep(20)


