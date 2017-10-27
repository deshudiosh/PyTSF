import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from html_id import HtmlId


def pjs_test():
    url = "http://192.168.1.2/Lists/Time%20Sheet%203D/NewForm.aspx?RootFolder=%2FLists%2FTime%20Sheet%203D&Source=http%3A%2F%2F192%2E168%2E1%2E2%2FLists%2FTime%2520Sheet%25203D%2Fcalendar%2Easpx"
    # url = "https://www.google.pl/"

    capa = DesiredCapabilities.PHANTOMJS
    capa['phantoms.page.settings.userName'] = "pawelgrz"
    capa['phantoms.page.settings.userPassword'] = "p4w3l"

    driver = webdriver.PhantomJS(executable_path="./drivers/phantomjs.exe",
                                 service_log_path=os.path.devnull,
                                 desired_capabilities=capa)

    try:
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.presence_of_element_located(By.ID, HtmlId.klient))
        print("yhy")
    except:
        print("biach")


pjs_test()


