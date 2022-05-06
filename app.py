'''

source :

'''

from selenium import webdriver
import time
from dotenv import load_dotenv
import os

load_dotenv()

USER_NAME       = os.getenv("USER_NAME")
USER_PASSWORD   = os.getenv("USER_PASSWORD")
FILE_PATH       = os.getenv("FILE_PATH")
FEATURING       = os.getenv("FEATURING")
DESCRIPTION     = os.getenv("DESCRIPTION")

browser = webdriver.Chrome()

def startpy():


    browser.get('https://audiomack.com/upload/non-musical')

    time.sleep(2)
                #Enter login info:
    mailid = browser.find_element_by_name('email')

    mailid.send_keys(USER_NAME)

    mailid.submit()

    time.sleep(2)

    secret = browser.find_element_by_name('password')

    secret.send_keys(USER_PASSWORD)

    secret.submit()

    time.sleep(30)

    upload_file()

def upload_file():

    browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/label/div/input').send_keys(FILE_PATH)

    time.sleep(100)

    browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/ul/li/div/section/section/div/div[2]/div[2]/div/input').send_keys(FEATURING)

    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/ul/li/div/section/footer/button').click()

    time.sleep(5)

    browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/ul/li/div/section/section/div[1]/textarea').send_keys(DESCRIPTION)

    browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/ul/li/div/section/footer/button[2]').click()

    time.sleep(2)

    browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/ul/li/div/section/section/div[2]/input').click()

    browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/ul/li/div/section/footer/button[2]').click()


if __name__ == "__main__":

    startpy()