from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

try:
    driver.get("https://iqra.nust.edu.pk")
    print("Main page loaded.")

    online_admission_link = WebDriverWait(driver, timeout=10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "ONLINE ADMISSION"))
    )
    online_admission_link.click()
    print("Navigated to Online Admission page.")

    # Full Name field
    full_name = WebDriverWait(driver, timeout=10).until(
        EC.presence_of_element_located((By.ID, "firstname"))
    )
    full_name.send_keys("Abdullah Shah")
    print("Filled Full Name field:", full_name.get_attribute('value'))
    
    # Date Of Birth field
    dob_field = driver.find_element(By.ID, "dob")
    dob_field.send_keys("06-02-2003")
    print("Filled Date Of Birth field:", dob_field.get_attribute('value'))
        
    # Religion field
    religion = driver.find_element(By.ID, "religion")
    religion.send_keys("Islam")
    print("Filled Religion field:", religion.get_attribute('value'))

    # Father's Name field
    father_name = driver.find_element(By.ID, "father_name")
    father_name.send_keys("Syed Muhammad Rizwan Alam")
    print("Filled Father's Name field:", father_name.get_attribute('value'))
    
    # Obtained Marks field
    obtained_marks = driver.find_element(By.ID, "custom_fields[studentacademic][33]")
    obtained_marks.send_keys("867")
    print("Filled Obtained Marks field:", obtained_marks.get_attribute('value'))

    # Board selection dropdown
    board_select = Select(driver.find_element(By.ID, "custom_fields[studentacademic][31]"))
    board_select.select_by_visible_text("Lahore Board")
    print("Selected Board:", board_select.first_selected_option.text)
    
    # NOC Issuance Date field
    noc_issuance_date = driver.find_element(By.ID, "custom_fields[studentacademic][40]")
    noc_issuance_date.send_keys("10-05-2024")
    print("Filled NOC Issuance Date:", noc_issuance_date.get_attribute('value'))
    
    # Subject for Grade 9th (SSC-1) dropdown
    subject_select = Select(driver.find_element(By.ID, "custom_fields[studentgroup][36]"))
    subject_select.select_by_visible_text("Computer Science")
    print("Selected Physics & Chemistry for Grade 9th (SSC-1) as:", subject_select.first_selected_option.text)

    # Blood Group dropdown
    blood_group_select = Select(driver.find_element(By.ID, "custom_fields[studenthealth][9]"))
    blood_group_select.select_by_visible_text("B+")
    print("Selected Blood Group as:", blood_group_select.first_selected_option.text)

    # Click the Home link to return to the homepage
    home_link = WebDriverWait(driver, timeout=10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "HOME"))
    )
    home_link.click()
    print("Clicked on Home page link.")

    current_url = driver.current_url
    if current_url == "https://iqra.nust.edu.pk/frontend":
        print("Successfully returned to the homepage: ", current_url)
    else:
        print("Failed to return to the correct homepage. Current URL:", current_url)

finally:
    driver.quit()
