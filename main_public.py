
import time
import random
import os
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome()

def check_time():
    localtime = time.localtime(time.time())
    hour = localtime[3]
    minute = localtime[4]
    wday = localtime[6]
#    print ("hour :", hour)
#    print ("minute :", minute)
#    print ("wday :", wday)
    if (wday < 5):
        if ((hour >= 8) and (minute > 0)):
            print ('wday =' +str(wday) + ' hour' + str(hour))
            return True,wday
    return False,wday

def open_web():
    '''
    開啟頁面
    '''
    print ('開啟頁面')
    #開啟web頁面
    driver.get('https://www.google.com.tw/')
    
    print ('輸入帳號')
    #找到ID欄位 
    id_element = driver.find_element_by_name("pnlno")
    print (id_element)
    #輸入ID
    id_element.send_keys("000123456")
    
    print ('輸入密碼')
    #找到Password欄位
    pw_element = driver.find_element_by_name("sidpassword")
    print (pw_element)
    #輸入Password
    pw_element.send_keys("N$7894@")
    
    print ('點選登入按鈕')
    #找到登入按鈕
    login_btn = driver.find_element_by_name("loginbtn")
    print (login_btn)
    #點選登入按鈕
    login_btn.click()

    print ('登入成功!')
    time.sleep(5)
    
    print ('選擇居家辦公')
    # 選擇居家辦公
    # driver.find_element_by_xpath('//*[@id="tempeForm"]/fieldset/div[2]/div/label[2]').click
    # element = driver.find_element_by_id('wkTypeRadio_2')
    # 公司上班
    element = driver.find_element_by_xpath('//*[@id="tempeForm"]/fieldset/div[2]/div/label[1]')
    # 居家辦公
    # element = driver.find_element_by_xpath('//*[@id="tempeForm"]/fieldset/div[2]/div/label[2]')
    print (element)
    element.click()

    print ('輸入溫度')
    #找到溫度欄位
    element = driver.find_element_by_name("temperature")
    print (element)
    # 小數位數隨機亂數3~8
    r = random.randint(3, 8)
    #輸入溫度
    element.send_keys("36."+ str(r))
    
    print ('點選儲存按鈕')
    #找到儲存按鈕
    save_btn = driver.find_element_by_name("savebtn")
    print (save_btn)
    #點選儲存按鈕
    save_btn.click()

    print ('完成!')

open_web()





