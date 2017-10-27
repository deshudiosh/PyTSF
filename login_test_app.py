from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# FIREFOX DRIVER
profile = FirefoxProfile()
# profile.set_preference("network.http.phishy-userpass-length", 255)
# profile.set_preference("network.automatic-ntlm-auth.trusted-uris", "192.168.1.2")
driver = webdriver.Firefox(firefox_profile=profile, executable_path="./geckodriver.exe")
driver.set_window_rect(30, 30, 800, 1000)


def try_login():
    # driver.get("http://192.168.1.2/default.aspx")
    # driver.get("http://192.168.1.2/Lists/Time%20Sheet%203D/calendar.aspx")
    # driver.get("http://192.168.1.2/Lists/Time%20Sheet%203D/NewForm.aspx?RootFolder=%2FLists%2FTime%20Sheet%203D&Source=http%3A%2F%2F192%2E168%2E1%2E2%2FLists%2FTime%2520Sheet%25203D%2Fcalendar%2Easpx")
    # driver.get("http://pawelgrz:p4w3l@192.168.1.2/Lists/Time%20Sheet%203D/calendar.aspx")
    driver.get("http://pawelgrz:p4w3l@192.168.1.2/Lists/Time%20Sheet%203D/NewForm.aspx?RootFolder=%2FLists%2FTime%20Sheet%203D&Source=http%3A%2F%2F192%2E168%2E1%2E2%2FLists%2FTime%2520Sheet%25203D%2Fcalendar%2Easpx")

    # # establish driver and login
    # try:
    #     wait = WebDriverWait(driver, 5)
    #     wait.until(EC.alert_is_present())
    #     alert = driver.switch_to.alert
    #     # print(alert)
    #     alert.send_keys("pawelgrz" + Keys.TAB + "p4w3l")
    #     sleep(1)  # wait, cause otherwise alert reappears if accepted too fast
    #     alert.accept()
    #     print("Logged In")
    #
    # except:
    #     print("Not Logged In...")
    sleep(2)
    # driver.find_element_by_id("zz10_NewMenu").click()

    sleep(20)


try_login()
