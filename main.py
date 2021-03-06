from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

rywebpage='http://automated.pythonanywhere.com/login/'
loginfield='id_username'
pwfield='id_password'
loginname='automated'
password='automatedautomated'
clickme='/html/body/nav/div/a'

def getwebpage(rywebpath):
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

def main(rywebpage,loginfield,loginname,pwfield,password,clickme):
  """ Logs in to a web page and clicks a link """
  driver=getwebpage(rywebpage)
  driver.get(rywebpage)
  driver.find_element(by='id', value=loginfield).send_keys(loginname)
  driver.find_element(by='id', value=pwfield).send_keys(password+Keys.RETURN)
  driver.find_element(by='xpath', value=clickme).click
  time.sleep(2)
  return driver

print(main(rywebpage,loginfield,loginname,pwfield,password,clickme).current_url)