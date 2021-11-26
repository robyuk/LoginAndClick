from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt

rywebpage='http://automated.pythonanywhere.com/login/'
loginfield='id_username'
pwfield='id_password'
loginname='automated'
password='automatedautomated'
clickme='/html/body/nav/div/a'
id='displaytimer'
filename='temp.txt'

def chromedriver():
  #Set options to make web browsing easier
  options=webdriver.ChromeOptions()
  options.add_argument('disable-infobars')
  options.add_argument('start-maximized')
  options.add_argument('disable-dev-shm-usage')
  options.add_argument('no-sandbox')
  options.add_argument('disable-blink-features=AutomationControlled')
  options.add_experimental_option('excludeSwitches', ['enable-automation'])
  
  driver=webdriver.Chrome(options=options)
  return driver

def gettemp(text):
  """ Extract only the temperature from the text string """
  temp=float(text.split(": ")[1])
  return temp

def pagelogin(rywebpage,loginfield,loginname,pwfield,password):
  """ Logs in to a web page """
  driver=chromedriver()
  driver.get(rywebpage)
  driver.find_element(by='id', value=loginfield).send_keys(loginname)
  time.sleep(2)
  driver.find_element(by='id', value=pwfield).send_keys(password+Keys.RETURN)
  time.sleep(2)
  return driver

def main(rywebpage,loginfield,loginname,pwfield,password,clickme,id):
  """Log into a webpage, click a link, and scrape a value to a file"""
  driver=pagelogin(rywebpage,loginfield,loginname,pwfield,password)
  driver.find_element(by='xpath', value=clickme).click

  while True:
    with open(filename,'a') as file:
      timestamp=str(dt.now())
      element=driver.find_element(by='id', value=id)
      file.write(f'{timestamp.split(".")[0]} : {gettemp(element.text)}\n')
    time.sleep(2)

  return element


print(gettemp(main(rywebpage,loginfield,loginname,pwfield,password,clickme,id).text))