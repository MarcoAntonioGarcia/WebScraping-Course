import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service #Extra importation because we have deprecated methods

servicio=Service('./chromedriver')
driver = webdriver.Chrome(service=servicio) #with that we get the control of the chrome page
driver.get('https://www.olx.com.ar/autos_c378') #open the page where we need get the information


for i in range (3):
    try:
        
        button=WebDriverWait(driver, 200).until(
            #it going to get the event espected
            #in this case it take the time when the button is recharged
            EC.presence_of_element_located((By.XPATH, '//button[@data-aut-id="btnLoadMore"]'))
        )
        #we need rewrite the xpath to looking for the button because each time in the new page, it change but with the same path
        #button = driver.find_element("xpath",'//button[@data-aut-id="btnLoadMore"]') ya no lo necesito porque ya se consulto 
        button.click()
        #sleep(random.uniform(8.0,10.0)) #Random time is less eficient, it's why we going to use WebDirverWait

        WebDriverWait(driver, 200).until(
            #it going to get the event espected
            #in this case it take the time when the button is recharged
            EC.presence_of_all_elements_located((By.XPATH, '//li[@data-aut-id="itemBox"]//span[@data-aut-id="itemPrice"]'))
        )

    except:
        #we are using this because sometimes over the buton we will find some objets and the click is imposible
        #or only we will get a error in click and with that we going to break this click and finish the program
        print("ERROR")
        break 
    
autos=driver.find_elements("xpath",'//li[@data-aut-id="itemBox"]')

for auto in autos:
    precio = auto.find_element("xpath", './/span[@data-aut-id="itemPrice"]').text
    print(precio)
    description = auto.find_element("xpath",'.//span[@data-aut-id="itemTitle"]').text
    print(description)
print(len(autos))    

