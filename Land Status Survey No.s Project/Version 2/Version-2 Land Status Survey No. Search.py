#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Version 2

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

print("Please Wait...")
url = "https://dharani.telangana.gov.in/knowLandStatus"

# Initialize Chrome webdriver (you might need to install it)
    
chrome_options = Options()
chrome_options.add_argument("--headless")
    
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

def findDistrict(d):
    
    
    district_element = driver.find_element(By.ID, "districtID")  
    district_select = Select(district_element)
    
    print("Searching District...")
    
    for district_option in district_select.options:
        district = district_option.text
        if d in district:
            district_select.select_by_visible_text(district)
            break
            
    time.sleep(2)

def findMandal(m):
    print("Searching Mandal...")
    mandal_element = driver.find_element(By.ID, "mandalID")  
    mandal_select = Select(mandal_element)
    
    for mandal_option in mandal_select.options:
        mandal = mandal_option.text
        if m in mandal:
            mandal_select.select_by_visible_text(mandal)
            break
    time.sleep(2)

def findVillage(v):
    print("Searchin Village...")
    village_element = driver.find_element(By.ID, "villageId")  
    village_select = Select(village_element)
    
    for village_option in village_select.options:
        village = village_option.text
        if v in village:
            village_select.select_by_visible_text(village)
            break
            
    time.sleep(2)

def findSurveyNos():
    print("Collecting Survey No.s...")
    
    survey_element = driver.find_element(By.ID, "surveyIdselect")
    survey_select = Select(survey_element)
    
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
    district = input("Enter District ").title()
    mandal = input("Enter Mandal ").title()
    village = input("Enter Village ").title()
    
    findDistrict(district)
    findMandal(mandal)
    findVillage(village)
    
    result = findSurveyNos()
    print()
    print('Survey Numbers:')
    [print(item) for item in result[1:]]
    
main()


# In[ ]:





# In[ ]:




