from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from html_id import HtmlId

def fill(months, month_idx, days_idxes):
    days_to_fill = [day for idx in days_idxes for day in months[month_idx].days if idx == day.date.day]

    # for day in days_to_fill:


def fill_day(day):
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get("file:///Y:/Python/PyTSF/timesheet_form.html")
    # driver.get("http://pawelgrz:p4w3l@192.168.1.2/Lists/Time%20Sheet%203D/calendar.aspx")
    # assert "Python" in driver.title
    # elem = driver.find_element_by_name("q")

    # Click 'new' button
    # driver.find_element_by_id("zz10_NewMenu").click()

    kategoria = driver.find_element_by_id(HtmlId.kategoria)
    klient = driver.find_element_by_id(HtmlId.klient)
    project = driver.find_element_by_id(HtmlId.project)
    osoba_zlecajaca = driver.find_element_by_id(HtmlId.osoba_zlecajaca)
    developer = driver.find_element_by_id(HtmlId.developer)
    rodzaj_czynnosci = driver.find_element_by_id(HtmlId.rodzaj_czynnosci)
    faza = driver.find_element_by_id(HtmlId.faza)

    start_date = driver.find_element_by_id(HtmlId.start_date)
    start_hours = Select(driver.find_element_by_id(HtmlId.start_hours))
    start_minutes = Select(driver.find_element_by_id(HtmlId.start_minutes))
    end_date = driver.find_element_by_id(HtmlId.end_date)
    end_hours = Select(driver.find_element_by_id(HtmlId.end_hours))
    end_minutes = Select(driver.find_element_by_id(HtmlId.end_minutes))

    description = driver.find_element_by_id(HtmlId.description)
    all_day_event = driver.find_element_by_id(HtmlId.all_day_event)


    # print(kategoria.tag_name)
    # print(klient.tag_name)
    # print(project.tag_name)
    # print(osoba_zlecajaca.tag_name)
    # print(developer.tag_name)
    # print(rodzaj_czynnosci.tag_name)
    # print(faza.tag_name)
    # print(start_date.tag_name)
    # print(start_hours.tag_name)
    # print(start_minutes.tag_name)
    # print(end_date.tag_name)
    # print(end_hours.tag_name)
    # print(end_minutes.tag_name)
    # print(description.tag_name)
    # print(all_day_event.tag_name)

    start_date.clear()
    start_date.send_keys(str(day.date))
    set_time(start_hours, day.start_time, True)
    set_time(start_minutes, day.start_time, False)
    end_date.clear()


    # driver.close()


def set_time(element: Select, time: datetime, is_hour: bool):
    element.select_by_visible_text(str(time.hour) + ":" if is_hour else str(time.minute))