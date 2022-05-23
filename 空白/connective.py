import time
from tkinter.ttk import PanedWindow
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
PATH = "./chromedriver.exe"
option=webdriver.ChromeOptions()
option.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1
  })      #權限賦予，上到下依序為麥克風，鏡頭，GPS，Google權限彈跳視窗
option.add_argument("disable-infobars") 
driver = webdriver.Chrome(options=option)

def google_classroom(username,password,classroom_url,meet_url):
  driver.get(classroom_url)
  search=driver.find_element_by_id("identifierId")  #google帳號登入帳號部分
  search.send_keys(username)
  search.click()
  search.send_keys(Keys.ENTER)
  time.sleep(3)                                     #等待google動畫完成
  passwd=driver.find_element_by_name("password")    #google帳號登入密碼部分
  passwd.send_keys(password)
  passwd.click()
  passwd.send_keys(Keys.ENTER)
  time.sleep(3)
  driver.execute_script("window.open('');")           #開啟新分頁目標地址meetroom
  driver.switch_to_window(driver.window_handles[1])   #將網頁指定在第二頁
  driver.get(meet_url)
  config=driver.find_element(By.TAG_NAME,"body")      #關閉麥克風與鏡頭
  config.send_keys(Keys.CONTROL,"d")
  config.send_keys(Keys.CONTROL,"e")

def exit():
  driver.quit()

if __name__=="__main__":
  username="u010717@tcivs.tc.edu.tw"
  passwd="96379637"
  classroom_url="https://classroom.google.com/c/Mzg2MzI2Mjc3OTcz"
  meet_url="https://meet.google.com/hpf-bmww-poe?authuser=0&hs=179"
  google_classroom(username,passwd,classroom_url,meet_url)