from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def highlight(element):
    driver.execute_script("arguments[0].style.border='2px solid red'", element)

driver = webdriver.Chrome()

driver.get("https://www.amazon.com")

print("Waiting for page to load and CAPTCHA to appear...")
time.sleep(10)

input("Please solve the CAPTCHA and press Enter to continue...")

css_elements1 = driver.find_elements(By.CSS_SELECTOR, ".s-min-slot .s-result-item")
css_elements2 = driver.find_elements(By.CSS_SELECTOR, ".s-min-slot .s-result-item")

hyperlink_elements1 = driver.find_elements(By.LINK_TEXT, "Amazon Basics")
hyperlink_elements2 = driver.find_elements(By.PARTIAL_LINK_TEXT, "Deals")

xpath_elements1 = driver.find_elements(By.XPATH, "//h2[@class='s-size-mini s-spacing-none s-color-base s-line-clamp-2']")
xpath_elements2 = driver.find_elements(By.XPATH, "//span[@class='a-price-whole'][1]") 

id_elements1 = driver.find_elements(By.ID, "nav-logo-sprites")
id_elements2 = driver.find_elements(By.ID, "nav-cart")

class_name_elements1 = driver.find_elements(By.CLASS_NAME, "nav-search-field")
class_name_elements2 = driver.find_elements(By.CLASS_NAME, "nav-input")

all_elements = (
    css_elements1 + css_elements2 +
    hyperlink_elements1 + hyperlink_elements2 +
    xpath_elements1 + xpath_elements2 +
    id_elements1 + id_elements2 +
    class_name_elements1 + class_name_elements2
)

for element in all_elements:
    highlight(element)
    print(element.text)
    time.sleep(2)

driver.quit()