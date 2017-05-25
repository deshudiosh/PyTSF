from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def fill(months, month_idx, days_idxes):
    days_to_fill = [day for idx in days_idxes for day in months[month_idx].days if idx == day.date.day]

    # for day in days_to_fill:


def fill_day(day):
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get("http://pawelgrz:p4w3l@192.168.1.2/Lists/Time%20Sheet%203D/calendar.aspx")
    # assert "Python" in driver.title
    # elem = driver.find_element_by_name("q")

    # Click 'new' button
    driver.find_element_by_id("zz10_NewMenu").click()

    kategoria = driver.find_element_by_id("ctl00_m_g_7c2ce97f_8ac4_4b04_bee8_08dd2b1efaeb_ctl00_ctl04_ctl00_ctl00_ctl00_ctl04_ctl00_DropDownChoice")
    print(kategoria)




    # driver.close()
    while True:
        pass

