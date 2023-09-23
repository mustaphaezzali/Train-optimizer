import multiprocessing
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as uc

def scraping_direct(trajet,confort):

    

    DRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(DRIVER_PATH)
    


    driver.maximize_window()

    driver.get(trajet[4])

    try:
        origin = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/section/div[1]/div[2]/main/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div")))
    except:
        driver.quit()

    try:
        origin = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ant-col-xxl-12")))
    except:
        driver.quit()

    if confort == "1èreclasse":
        gamme=driver.find_element(By.XPATH,"/html/body/div/section/div[1]/div[2]/main/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/label[1]")
        gamme.click()
    elif confort == "Lit single":
        gamme=driver.find_element(By.XPATH,"/html/body/div/section/div[1]/div[2]/main/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/label[3]")
        gamme.click()
    
    search=driver.find_element(By.XPATH,"/html/body/div/section/div[1]/div[2]/main/div/div/div[2]/div/div/div[2]/div/div/div/button")
    search.click()

    time.sleep(15)

    try:
        origin = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#root > section > div.ant-row > div.ant-col > main > div > div > div > div.ant-col.ant-col-xs-24.ant-col-md-24.ant-col-lg-16.ant-col-xl-16.ant-col-xxl-18 > div > div.ant-card.trip-card-wrapper > div.ant-card-body")))
    except:
        driver.quit()

    cards=driver.find_elements(By.XPATH,"//div[@class='ant-row trips']")
    for card in cards:
        string_ints = [str(int) for int in trajet[1]]
        if card.find_element(By.XPATH,".//label[@class='date']").text==":".join(string_ints):
            type=card.find_element(By.XPATH,".//span[@class='TripCardFooter_Correspondance_description_span']").text
            price=card.find_element(By.XPATH,".//label[@class='price']").text
            trajet.append(type)
            trajet.append(price)
            break


def scraping_voyages(trajet1,trajet2,confort):

    DRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(DRIVER_PATH)

    driver.maximize_window()

    driver.get(trajet1[4])

    try:
        origin = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/section/div[1]/div[2]/main/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div")))
    except:
        driver.quit()

    try:
        origin = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ant-col-xxl-12")))
    except:
        driver.quit()

    if confort == "1èreclasse":
        gamme=driver.find_element(By.XPATH,"/html/body/div/section/div[1]/div[2]/main/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/label[1]")
        gamme.click()
    elif confort == "Lit single":
        gamme=driver.find_element(By.XPATH,"/html/body/div/section/div[1]/div[2]/main/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/label[3]")
        gamme.click()
    
    search=driver.find_element(By.XPATH,"/html/body/div/section/div[1]/div[2]/main/div/div/div[2]/div/div/div[2]/div/div/div/button")
    search.click()


    driver.switch_to.new_window()
    driver.get(trajet2[4])

    try:
        origin = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/section/div[1]/div[2]/main/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div")))
    except:
        driver.quit()

    try:
        origin = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ant-col-xxl-12")))
    except:
        driver.quit()

    if confort == "1èreclasse":
        gamme=driver.find_element(By.XPATH,"/html/body/div/section/div[1]/div[2]/main/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/label[1]")
        gamme.click()
    elif confort == "Lit single":
        gamme=driver.find_element(By.XPATH,"/html/body/div/section/div[1]/div[2]/main/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/label[3]")
        gamme.click()
    
    search=driver.find_element(By.XPATH,"/html/body/div/section/div[1]/div[2]/main/div/div/div[2]/div/div/div[2]/div/div/div/button")
    search.click()

    tabs = driver.window_handles
    driver.switch_to.window(tabs[0])
    time.sleep(15)

    try:
        origin = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#root > section > div.ant-row > div.ant-col > main > div > div > div > div.ant-col.ant-col-xs-24.ant-col-md-24.ant-col-lg-16.ant-col-xl-16.ant-col-xxl-18 > div > div.ant-card.trip-card-wrapper > div.ant-card-body")))
    except:
        driver.quit()

    cards=driver.find_elements(By.XPATH,"//div[@class='ant-row trips']")
    for card in cards:
        string_ints = [str(int) for int in trajet1[1]]
        if card.find_element(By.XPATH,".//label[@class='date']").text==":".join(string_ints):
            type=card.find_element(By.XPATH,".//span[@class='TripCardFooter_Correspondance_description_span']").text
            price=card.find_element(By.XPATH,".//label[@class='price']").text
            trajet1.append(type)
            trajet1.append(price)
            break

    driver.switch_to.window(tabs[1])

    try:
        origin = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#root > section > div.ant-row > div.ant-col > main > div > div > div > div.ant-col.ant-col-xs-24.ant-col-md-24.ant-col-lg-16.ant-col-xl-16.ant-col-xxl-18 > div > div.ant-card.trip-card-wrapper > div.ant-card-body")))
    except:
        driver.quit()

    cards=driver.find_elements(By.XPATH,"//div[@class='ant-row trips']")
    for card in cards:
        string_ints2 = [str(int) for int in trajet2[1]]
        if card.find_element(By.XPATH,".//label[@class='date']").text==":".join(string_ints2):
            type=card.find_element(By.XPATH,".//span[@class='TripCardFooter_Correspondance_description_span']").text
            price=card.find_element(By.XPATH,".//label[@class='price']").text
            trajet2.append(type)
            trajet2.append(price)
            break



# trajet1=['RABAT_AGDAL', [15, 12], 'KENITRA', [15, 51], 'https://www.oncf-voyages.ma/recherche-disponibilites/229/250/1654611120']

# trajet2=['KENITRA', [16, 20], 'TANGER', [17, 10], 'https://www.oncf-voyages.ma/recherche-disponibilites/250/303/1654615200']
# scraping_voyages(trajet1,trajet2,"1èreclasse")

# print(trajet1)
# print(trajet2)