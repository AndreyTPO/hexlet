from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('C:/Users/AD-min/Downloads/Driver/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://qa.neapro.site/login")
driver.set_window_size(1024, 600)
driver.minimize_window()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").click()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(1) input").send_keys("night.manager00@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").click()
driver.find_element(By.CSS_SELECTOR, ".fieldset:nth-child(2) input").send_keys("AndreyKA2309")
driver.find_element(By.CSS_SELECTOR, ".btn").click()
