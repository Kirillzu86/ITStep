from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# Настройки Selenium
chrome_options = Options()

# Запуск в фоне
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu") 

# Оптимизация
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-software-rasterizer")

# Отключение проверки на сертификат SSL
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")

# Отключает ограничения безопасности браузера
chrome_options.add_argument("--disable-web-security")

# Запуск браузера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Открываем сайт
url = "https://aliexpress.ru/"
driver.get(url)
time.sleep(random.uniform(3, 5))  # Ждем загрузки страницы

# Убираем флаг Selenium
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Скроллим страницу для загрузки всех элементов
for _ in range(3):
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(random.uniform(1, 3))

# Извлекаем цены
price_elements = driver.find_elements(By.CSS_SELECTOR, "div[class*='price']")

# Получаем список цен
prices = [price.text for price in price_elements if price.text.strip()]

# Закрываем браузер
driver.quit()

# Выводим цены
for price in prices:
    print(price)
