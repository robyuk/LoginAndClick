from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt

rywebpage = 'https://titan22.com/account/login?return_url=%2Faccount'
loginfield = 'CustomerEmail'
pwfield = 'CustomerPassword'
loginname = 'youngr2000-titan22@yahoo.com'
password = 'PnQf8hVJanCBhxiLCCw5'
clickme = '//*[@id="shopify-section-footer"]/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a'


def chromedriver():
    #Set options to make web browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_argument('disable-blink-features=AutomationControlled')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    driver = webdriver.Chrome(options=options)
    return driver


def gettemp(text):
    """ Extract only the temperature from the text string """
    temp = float(text.split(": ")[1])
    return temp


def pagelogin(rywebpage, loginfield, loginname, pwfield, password):
    """ Logs in to a web page """
    driver = chromedriver()
    driver.get(rywebpage)
    driver.find_element(by='id', value=loginfield).send_keys(loginname)
    time.sleep(2)
    driver.find_element(by='id',
                        value=pwfield).send_keys(password + Keys.RETURN)
    time.sleep(2)
    return driver


def main(rywebpage, loginfield, loginname, pwfield, password, clickme):
    """Log into a webpage, click a link, and scrape a value to a file"""
    driver = pagelogin(rywebpage, loginfield, loginname, pwfield, password)
    time.sleep(19)
    driver.find_element(by='xpath', value=clickme).click
    print(driver.current_url)

    #
print(main(rywebpage, loginfield, loginname, pwfield, password, clickme))