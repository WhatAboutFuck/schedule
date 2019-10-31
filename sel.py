from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from config import link
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

def get_scrin(x):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    
    group = driver.find_element_by_id('ctl00_MainContent_ASPxPageControl1_grGroup_DXFREditorcol0_I')
    group.send_keys(x)


    driver.implicitly_wait(4)
    
    try:
        driver.find_element_by_link_text(x).click()
    except NoSuchElementException:
        driver.close()
        return False
    driver.execute_script("window.scrollTo(0, 1080)")
    driver.execute_script("document.body.style.zoom='75%'") 
    driver.implicitly_wait(4)
    driver.get_screenshot_as_file('sheddule.png')
    driver.close()
    s = open('sheddule.png','rb')

    return s 

def get_stuff(u):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    driver.find_element_by_id('ctl00_MainContent_ASPxPageControl1_T2T').click()
    driver.implicitly_wait(4)
    k = driver.find_element_by_id('ctl00_MainContent_ASPxPageControl1_gvPrep_DXFREditorcol0_I')
    k.send_keys(u)
    driver.implicitly_wait(4)
    try:
        driver.find_element_by_link_text(u).click()
    except NoSuchElementException:
        driver.close()
        return False
    driver.execute_script("window.scrollTo(0, 1080)")
    driver.execute_script("document.body.style.zoom='75%'") 
    driver.get_screenshot_as_file('stuff.png')
    driver.close()
    st = open('stuff.png','rb')
    return st

