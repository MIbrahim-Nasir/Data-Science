#!/usr/bin/env python
# coding: utf-8

# In[7]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def findSurveyNos(d, m ,v):
    url = "https://dharani.telangana.gov.in/knowLandStatus"

    # Initialize Chrome webdriver (you might need to install it)
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    
    print("Searching District...")
    
    district_element = driver.find_element(By.ID, "districtID")  
    district_select = Select(district_element)
    district_select.select_by_visible_text(d)
    
    time.sleep(2)
    
    print("Searching Mandal...")

    mandal_element = driver.find_element(By.ID, "mandalID")  
    mandal_select = Select(mandal_element)
    mandal_select.select_by_visible_text(m)
    
    time.sleep(2)
    
    print("Searchin Village...")

    village_element = driver.find_element(By.ID, "villageId")  
    village_select = Select(village_element)
    village_select.select_by_visible_text(v)
    
    time.sleep(2)
    
    print("Collecting Survey No.s...")
    
#     wait = WebDriverWait(driver, 10)
#     wait.until(EC.presence_of_element_located((By.ID, "surveyIdselect")))
    
    survey_element = driver.find_element(By.ID, "surveyIdselect")
    survey_select = Select(survey_element)
#     survey_option = survey_select.options[1]
#     survey = survey_option.text
    surveys = []
    for survey_option in survey_select.options:
        survey = survey_option.text
        surveys.append(survey)
        survey_select.select_by_visible_text(survey)
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "surveyIdselect")))
            
    driver.quit()
    
    return surveys

def main():
    district = input("Enter District")
    mandal = input("Enter Mandal")
    village = input("Enter Village")
    
    result = findSurveyNos(district, mandal, village)
    
    [print(item) for item in result[1:]]

if __name__ == '__main__':
    main()
    
# SAMPLE INPUT
# District - Adilabad|ఆదిలాబాద్
# Mandal - Adilabad (Rural)|ఆదిలాబాద్ (రూరల్)
# Village - Ankapoor|అంకాపూర్

