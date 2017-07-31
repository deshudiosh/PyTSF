import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from gsheets_data_parser import Job
from html_id import HtmlId


def fill(months, month_idx, days_idxes):
    days_to_fill = [day for idx in days_idxes for day in months[month_idx].days if idx == day.date.day]

    fill_days(days_to_fill)


def fill_days(days: list):
    driver = webdriver.Chrome("./chromedriver.exe")
    for day in days:
        for job in day.jobs:
            fill_job(driver, job)

def fill_job(driver: webdriver,  job: Job):

    # TODO: move timesheet login and password to Settings
    # driver.get(Path("timesheet_form.html").resolve().as_posix())
    driver.get("http://pawelgrz:p4w3l@192.168.1.2/Lists/Time%20Sheet%203D/calendar.aspx")
    driver.find_element_by_id("zz10_NewMenu").click()

    # Elements
    kategoria = Select(driver.find_element_by_id(HtmlId.kategoria))
    klient = driver.find_element_by_id(HtmlId.klient)
    project = driver.find_element_by_id(HtmlId.project)
    osoba_zlecajaca = driver.find_element_by_id(HtmlId.osoba_zlecajaca)
    developer = Select(driver.find_element_by_id(HtmlId.developer))
    rodzaj_czynnosci = Select(driver.find_element_by_id(HtmlId.rodzaj_czynnosci))
    faza = Select(driver.find_element_by_id(HtmlId.faza))

    start_date = driver.find_element_by_id(HtmlId.start_date)
    start_hours = Select(driver.find_element_by_id(HtmlId.start_hours))
    start_minutes = Select(driver.find_element_by_id(HtmlId.start_minutes))
    end_date = driver.find_element_by_id(HtmlId.end_date)
    end_hours = Select(driver.find_element_by_id(HtmlId.end_hours))
    end_minutes = Select(driver.find_element_by_id(HtmlId.end_minutes))

    description = driver.find_element_by_id(HtmlId.description)
    all_day_event = driver.find_element_by_id(HtmlId.all_day_event)

    ok_button = driver.find_element_by_id(HtmlId.ok_button)

    # Assign values
    kategoria.select_by_visible_text(job.kategoria)
    klient.send_keys(job.klient)
    project.send_keys(job.project)
    osoba_zlecajaca.send_keys(job.osoba_zlecajaca)
    developer.select_by_visible_text(job.developer)
    rodzaj_czynnosci.select_by_visible_text(job.rodzaj_czynnosci)
    faza.select_by_visible_text(job.faza)

    description.send_keys(job.description)

    if job.all_day_event:
        driver.execute_script("".join(["document.getElementById('",
                                       HtmlId.all_day_event,
                                       "').setAttribute('checked', 'checked')"]))
    else:
        start_hours.select_by_visible_text(job.start_hours)
        start_minutes.select_by_visible_text(job.start_minutes)
        end_hours.select_by_visible_text(job.end_hours)
        end_minutes.select_by_visible_text(job.end_minutes)

    start_date.clear()
    start_date.send_keys(job.start_date)
    end_date.clear()
    end_date.send_keys(job.end_date)

    ok_button.send_keys("\n")

    # time.sleep(5)
