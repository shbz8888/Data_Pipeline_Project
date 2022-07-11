
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get("https://gorillamind.com/")




def load_and_accept_cookies() -> webdriver.Chrome:
    '''
    Open Zoopla and accept the cookies
    
    Returns
    -------
    driver: webdriver.Chrome
        This driver is already in the Zoopla webpage
    '''
    driver = webdriver.Chrome() 
    driver.get("https://gorillamind.com/")
    link = driver.find_element(By.LINK_TEXT,"All Products")
    link.click()
    link2 = driver.find_element(By.CLASS_NAME,"sc-75msgg-0 RlRPc close-button cw-close")
    link2.click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"sc-75msgg-0 RlRPc close-button cw-close")))
        element.click()
    except:
        driver.quit() 

    return

load_and_accept_cookies()





    