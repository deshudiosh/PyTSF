from datetime import datetime

import pygsheets


class Day:
    def __init__(self, rowData):
        """ Unpack row data to properties, BUT omit 6th column """
        del rowData[5]
        self.date, \
        self.start_time, \
        self.start_lunch, \
        self.end_lunch, \
        self.end_time, \
        self.work1, \
        self.work2 = rowData
        self._validate()

    def _validate(self):
        # convert date to datetime (should be done earlier?, yea.)

        # convert times to datetimes, assign date from "date" property above
        # round to 5min step
        # CHECK IN NOT NEXT DAY !! (if so, add one, or two, hah)

        # validate work1/2 somehow (num of elements?)
        # parse to Work class, containing properties (klient, osoba zlecajaca, itd)

        # assign "isValid" value!
        pass


class Month:
    def __init__(self, sheetData):
        self.days = []
        for row in sheetData:
            # If first cell contains date, parse as day
            if isDate(row[0]):
                self.days.append(Day(row))


def getMonths(settings):
    gc = pygsheets.authorize()
    sh = gc.open_by_url(settings["spreadsheetURL"])

    months = []

    # If cell A1 is contains date, parse worksheet as month
    for worksheet in sh.worksheets():
        if isDate(worksheet.get_value("A1")):
            cells = worksheet.get_values(start=(1, 1), end=(31, 8), include_all=True)
            months.append(Month(cells))


def isDate(dateStr):
    try:
        date = datetime.strptime(dateStr, "%Y-%m-%d")
    except:
        date = None

    return isinstance(date, datetime)
