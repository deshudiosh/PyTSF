from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from gsheets_data_parser import Job
from html_id import HtmlId


def fill(months, month_idx, days_idxes):
    days_to_fill = [day for idx in days_idxes for day in months[month_idx].days if idx == day.date.day]

    fill_days(days_to_fill)


def fill_days(days: list):
    driver = webdriver.Firefox(executable_path="./geckodriver.exe")
    driver.set_window_rect(80, 30, 800, 1100)


    for day in days:
        for job in day.jobs:
            fill_job(driver, job)


def fill_job(driver: webdriver,  job: Job):

    # TODO: move timesheet login and password to Settings
    driver.get("http://pawelgrz:p4w3l@192.168.1.2/Lists/Time%20Sheet%203D/NewForm.aspx?RootFolder=%2FLists%2FTime%20Sheet%203D&Source=http%3A%2F%2F192%2E168%2E1%2E2%2FLists%2FTime%2520Sheet%25203D%2Fcalendar%2Easpx")

    try:
        # element = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, HtmlId.kategoria)))

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
        # ok_button = driver.find_element_by_xpath("//input[@value='OK']")


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

        # print(dir(ok_button))
        sleep(1)
        # ok_button.screenshot_as_png("c:/xxx.png")
        ok_button.send_keys("\n")
        ok_button.send_keys("\n")
        ok_button.click()
        ok_button.click()
        print(ok_button.is_selected())


    except:
        print("CHUUUJ")


