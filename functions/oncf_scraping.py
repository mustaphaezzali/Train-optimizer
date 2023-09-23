import multiprocessing
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from functions import shortest_path
from datetime import datetime
#from functions.pathCHOICEdone import path_choice


depart = "RABAT AGDAL"
arrivee = "TANGER"
date_depart= "02/06/2022"


night=False            #00-06
morning=False          #06-12
afternoon=True         #12-19
evening=False          #19-00

def periode(datedepart):
    if datedepart>="00:00" and datedepart<"06:00" :
        periodes=[1,0,0,0]
    elif datedepart>="06:00" and datedepart<"12:00" :
        periodes=[0,1,0,0]
    elif datedepart>="12:00" and datedepart<"19:00" : 
        periodes=[0,0,1,0]
    elif datedepart>="19:00":
        periodes=[0,0,0,1]
    return periodes

    



def scrap_oncf(depart,arrivee,date_depart,periode,temps):

    date_depart=date_depart+" "+temps


    DRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(DRIVER_PATH)

    #get the path
    #path=path_choice(depart, arrivee)
    path = shortest_path.shortest_path(shortest_path.graph, depart, arrivee)
    n = len(path)
    driver.get("https://www.oncf.ma/fr/Horaires")

    for i in range(0,2*(n-2)-1):
        driver.switch_to.new_window()
        driver.get("https://www.oncf.ma/fr/Horaires")

    tabs = driver.window_handles
    driver.switch_to.new_window()
    driver.get("https://www.oncf.ma/fr/Horaires")

    try:
        origin = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/main/div/div[2]/div/div/div/div/div/form/div[1]"))
        )
    except:
        driver.quit()

    for i in range(1,n-1):
        #with driver:

            driver.switch_to.window(tabs[2*i-2])

            try:
                origin = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div/div/div/div/div/form/div[1]"))
                )
            except:
                driver.quit()

            style=driver.find_element(By.CSS_SELECTOR,"#autocomplete")
            driver.find_element(By.CSS_SELECTOR,"#autocomplete").send_keys(path[0])
            time.sleep(1)
            list=driver.find_elements_by_xpath("//div[contains(@class, 'ui-menu-item-wrapper')]")
            print(list)
            for j in list:
                if (j.text==path[0]):
                    j.click()
                    break

            style1=driver.find_element(By.CSS_SELECTOR,"#autocomplete2")
            driver.find_element(By.CSS_SELECTOR,"#autocomplete2").send_keys(path[i])
            time.sleep(1)        
            list=driver.find_elements_by_xpath("//div[contains(@class, 'ui-menu-item-wrapper')]")
            print(list)
            for j in list:
                if (j.text==path[i+1]):
                    j.click()
                    break

            datepick="#datetimepickerDep"
            try:
                origin = WebDriverWait(driver, 5).until( 
                    EC.presence_of_element_located((By.CSS_SELECTOR, datepick))
                )
            except:
                driver.quit()

            aller = driver.find_element(By.CSS_SELECTOR,"#tab55 > div:nth-child(3) > div.form-checkbox.font11 > div:nth-child(2) > label")
            aller.click()  

            datepicker= driver.find_element(By.CSS_SELECTOR,"#datetimepickerDep")
            datepicker.click()
            datepicker.clear()
            datepicker.send_keys(date_depart)

            searchButton="#horaires-api > div > div > div > form > div.form-item.see-all.show-on-desktop > button"
            search=driver.find_element(By.CSS_SELECTOR,searchButton)
            search.click()

            
            driver.switch_to.window(tabs[2*i-1])

            try:
                origin = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div/div/div/div/div/form/div[1]"))
                )
            except:
                driver.quit()

            style=driver.find_element(By.CSS_SELECTOR,"#autocomplete")
            driver.find_element(By.CSS_SELECTOR,"#autocomplete").send_keys(path[i])
            time.sleep(1)
            list=driver.find_elements_by_xpath("//div[contains(@class, 'ui-menu-item-wrapper')]")
            print(list)
            for j in list:
                if (j.text==path[i]):
                    j.click()
                    break

            style1=driver.find_element(By.CSS_SELECTOR,"#autocomplete2")
            driver.find_element(By.CSS_SELECTOR,"#autocomplete2").send_keys(path[-1])
            time.sleep(1)        
            list=driver.find_elements_by_xpath("//div[contains(@class, 'ui-menu-item-wrapper')]")
            print(list)
            for j in list:
                if (j.text==path[i+1]):
                    j.click()
                    break

            datepick="#datetimepickerDep"
            try:
                origin = WebDriverWait(driver, 5).until( 
                    EC.presence_of_element_located((By.CSS_SELECTOR, datepick))
                )
            except:
                driver.quit()

            aller = driver.find_element(By.CSS_SELECTOR,"#tab55 > div:nth-child(3) > div.form-checkbox.font11 > div:nth-child(2) > label")
            aller.click()  

            datepicker= driver.find_element(By.CSS_SELECTOR,"#datetimepickerDep")
            datepicker.click()
            datepicker.clear()
            datepicker.send_keys(date_depart)

            searchButton="#horaires-api > div > div > div > form > div.form-item.see-all.show-on-desktop > button"
            search=driver.find_element(By.CSS_SELECTOR,searchButton)
            search.click()



    tabs = driver.window_handles
    driver.switch_to.window(tabs[-1])

    try:
        origin = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div/div/div/div/div/form/div[1]"))
        )
    except:
        driver.quit()

    style=driver.find_element(By.CSS_SELECTOR,"#autocomplete")
    driver.find_element(By.CSS_SELECTOR,"#autocomplete").send_keys(path[0])
    time.sleep(1)
    list=driver.find_elements_by_xpath("//div[contains(@class, 'ui-menu-item-wrapper')]")
    print(list)
    for j in list:
        if (j.text==path[i]):
            j.click()
            break

    style1=driver.find_element(By.CSS_SELECTOR,"#autocomplete2")
    driver.find_element(By.CSS_SELECTOR,"#autocomplete2").send_keys(path[-1])
    time.sleep(1)        
    list=driver.find_elements_by_xpath("//div[contains(@class, 'ui-menu-item-wrapper')]")
    print(list)
    for j in list:
        if (j.text==path[i+1]):
            j.click()
            break

    datepick="#datetimepickerDep"
    try:
        origin = WebDriverWait(driver, 5).until( 
            EC.presence_of_element_located((By.CSS_SELECTOR, datepick))
        )
    except:
        driver.quit()

    aller = driver.find_element(By.CSS_SELECTOR,"#tab55 > div:nth-child(3) > div.form-checkbox.font11 > div:nth-child(2) > label")
    aller.click()  

    datepicker= driver.find_element(By.CSS_SELECTOR,"#datetimepickerDep")
    datepicker.click()
    datepicker.clear()
    datepicker.send_keys(date_depart)

    searchButton="#horaires-api > div > div > div > form > div.form-item.see-all.show-on-desktop > button"
    search=driver.find_element(By.CSS_SELECTOR,searchButton)
    search.click()

    trajectories=[]
    for i in range(len(tabs)):
        if i%2==0:
            traj=[]
        trajectory=[]
        driver.switch_to.window(tabs[i])
        time.sleep(1)
        name=driver.find_element(By.CSS_SELECTOR,"body > div.container-large > main > div.block-horaires.block-spaced > div > div > div.block-horaires--info--relation > span.block-horaires--info--relation-detail").text
        names=name.split("-")
        for j in range(len(names)):
            names[j]=names[j].strip()
            names[j]=names[j].replace(" ","_")
        rows=driver.find_elements(By.XPATH,"//tr[@class='accordion-row']")
        for row in rows:
            travel_depart=row.find_element_by_xpath(".//div[@class='p-relative']").text
            travel_depart=travel_depart.replace('h',':')
            travel_depart=travel_depart.replace('min','')
            travel_arrive=row.find_element_by_xpath(".//td[@data-th='Arrivée']").text
            travel_arrive=travel_arrive.replace('h',':')
            travel_arrive=travel_arrive.replace('min','')
            buy=row.find_element_by_xpath(".//a[@class='button button-uppercase' and @target='_blank']").get_attribute('href')
            if (names[0].replace("_"," ")==depart and not((periode[0] and travel_depart>="00:00" and travel_depart<"06:00") or (periode[1] and travel_depart>="06:00" and travel_depart<"12:00") or (periode[2] and travel_depart>="12:00" and travel_depart<"19:00") or (periode[3] and travel_depart>="19:00"))):
                continue
            else:
                trajectory.append([names[0],travel_depart,names[1],travel_arrive,buy])
        if i!=len(tabs)-1:
            traj.append(trajectory)
        else:
            trajectories.append(trajectory)
        if i%2!=0:
            trajectories.append(traj)

    return trajectories


