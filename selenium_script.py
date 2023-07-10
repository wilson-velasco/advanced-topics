from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

import time as t
import os

user = os.getenv("githubUSER")
pswd = os.getenv("githubPSWD")

base_url = "https://www.github.com/"

def download_sql_files():
    '''Downloads all sql files from the database-exercises repo of a Codeup student'''
    driver = webdriver.Chrome(service = Service())
    driver.get(base_url + "login")
    driver.find_element(By.NAME, "login").send_keys(user)
    driver.find_element(By.NAME, "password").send_keys(pswd)
    driver.find_element(By.NAME, "commit").click()
    t.sleep(2)
    driver.get(base_url+user+"/database-exercises")
    len_paths = len(driver.find_elements(By.XPATH, "//a[@class='js-navigation-open Link--primary']"))
    
    for i in range(len_paths):
        driver.get(base_url+user+"/database-exercises")
        paths = driver.find_elements(By.XPATH, "//a[@class='js-navigation-open Link--primary']")
        if paths[i].text.endswith('sql'):
            paths[i].click()
            WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Download raw content']")))
            driver.find_element(By.XPATH, "//button[@aria-label='Download raw content']").click()
            t.sleep(2)
            driver.find_element(By.XPATH, "//a[@sx='[object Object]']").click()
            t.sleep(2)

def download_ipynb_files():
    '''Downloads all ipynb files from the regression-exercises repo of a Codeup student.'''
    driver = webdriver.Chrome(service = Service())
    driver.get(base_url + "login")
    driver.find_element(By.NAME, "login").send_keys(user)
    driver.find_element(By.NAME, "password").send_keys(pswd)
    driver.find_element(By.NAME, "commit").click()
    t.sleep(2)
    driver.get(base_url+user+"/regression-exercises") #repo link here
    len_paths = len(driver.find_elements(By.XPATH, "//a[@class='js-navigation-open Link--primary']"))
    
    for i in range(len_paths):
        driver.get(base_url+user+"/regression-exercises") #repo link here
        paths = driver.find_elements(By.XPATH, "//a[@class='js-navigation-open Link--primary']")
        if paths[i].text.endswith('ipynb'): #file extension here
            paths[i].click()
            WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Download raw content']")))
            driver.find_element(By.XPATH, "//button[@aria-label='Download raw content']").click()
            t.sleep(2)
            driver.find_element(By.XPATH, "//a[@sx='[object Object]']").click()
            t.sleep(2)

def download_files(repo, file_extension):
    '''Takes in the repo name and the file extension of the files you want to download as strings, and downloads those respective files
    from that repo.'''
    driver = webdriver.Chrome(service = Service())
    driver.get(base_url + "login")
    driver.find_element(By.NAME, "login").send_keys(user)
    driver.find_element(By.NAME, "password").send_keys(pswd)
    driver.find_element(By.NAME, "commit").click()
    t.sleep(2)
    driver.get(base_url+user+"/"+repo)
    len_paths = len(driver.find_elements(By.XPATH, "//a[@class='js-navigation-open Link--primary']"))
    
    for i in range(len_paths):
        driver.get(base_url+user+"/"+repo)
        paths = driver.find_elements(By.XPATH, "//a[@class='js-navigation-open Link--primary']")
        if paths[i].text.endswith(file_extension):
            paths[i].click()
            WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Download raw content']")))
            driver.find_element(By.XPATH, "//button[@aria-label='Download raw content']").click()
            t.sleep(2)
            driver.find_element(By.XPATH, "//a[@sx='[object Object]']").click()
            t.sleep(2)