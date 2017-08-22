import datetime

import sheetsapi


class Job(object):
    def __init__(self, start: datetime.datetime, end: datetime.datetime = None, data = None, is_free_day = False, is_lunch = False):
        self.is_free_day = is_free_day
        self.is_lunch = is_lunch

        if is_free_day:
            self.start_date = str(start)
            self.end_date = str(start)
        else:
            self.start_date = str(start.date())
            self.start_hours = Job._get_time_str(start, True)
            self.start_minutes = Job._get_time_str(start, False)
            self.end_date = str(end.date())
            self.end_hours = Job._get_time_str(end, True)
            self.end_minutes = Job._get_time_str(end, False)

        self.developer = "Nie dotyczy"

        # todo: get name from settings
        if is_free_day:
            self.kategoria = "Dzień wolny"
            self.klient = "Paweł Grzelak"
            self.project = "Dzień wolny"
            self.osoba_zlecajaca = "Paweł Grzelak"
            self.rodzaj_czynnosci = "Dzien wolny"
            self.faza = "Nie dotyczy"
            self.description = "Dzień wolny"
            self.all_day_event = True

        elif is_lunch:
            self.kategoria = "Lunch"
            self.klient = "Paweł Grzelak"
            self.project = "Lunch"
            self.osoba_zlecajaca = "Paweł Grzelak"
            self.rodzaj_czynnosci = "Lunch"
            self.faza = "Nie dotyczy"
            self.description = "Lunch"
            self.all_day_event = False

        elif data and len(data) == 4:
            self.kategoria = "Wizualizacje"
            self.klient = str(data[0])
            self.project = str(data[1])
            self.osoba_zlecajaca = str(data[2])
            self.rodzaj_czynnosci = "Modelowanie"
            self.faza = "Nie dotyczy"
            self.description = str(data[3])
            self.all_day_event = False

    @staticmethod
    def _get_time_str(time: datetime, is_hour: bool):
        # print(time.minute)
        h = str(time.hour) + ":"
        h = h if len(h) == 3 else "0" + h
        m = str(time.minute)
        m = m if len(m) == 2 else "0" + m
        return h if is_hour else m

    def __repr__(self):
        return str(self.__dict__)


class Day:
    def __init__(self, row_data):
        self.is_free_day = False

        self.date = as_date(row_data[0])

        self.start_time = Day._validate_time(row_data[1], self.date)
        self.start_lunch = Day._validate_time(row_data[2], self.date)
        self.end_lunch = Day._validate_time(row_data[3], self.date)
        self.end_time = Day._validate_time(row_data[4], self.date)

        self.work1 = self._validate_work(row_data[5])
        self.work2 = self._validate_work(row_data[6])

        # todo: consider removing is_valid and replace it with jobs[] length check
        self.is_valid = all([self.date, self.start_time, self.end_time, self.work1])

        self.has_lunch = all([self.start_lunch, self.end_lunch])
        self.single_job = self.work1 and not self.work2

        self.jobs = []

        self._create_jobs()

    def __repr__(self):
        return "<" + str(len(self.jobs)) + " -> " + str(self.jobs) + ">"

    def _create_jobs(self):
        """ Day schemes """
        # -> free day"""
        if self.is_free_day:
            self.jobs.append(Job(self.date, is_free_day=True))
            return

        # -> day with lunch
        if self.has_lunch:
            if self.single_job:  # -> work, lunch
                self.jobs.append(Job(self.start_time, self.start_lunch, self.work1))
                self.jobs.append(Job(self.start_lunch, self.end_lunch, is_lunch=True))
                self.jobs.append(Job(self.end_lunch, self.end_time, self.work1))
            else:  # -> work, lunch, work
                self.jobs.append(Job(self.start_time, self.start_lunch, self.work1))
                self.jobs.append(Job(self.start_lunch, self.end_lunch, is_lunch=True))
                self.jobs.append(Job(self.end_lunch, self.end_time, self.work2))
        # -> no lunch
        else:
            # -> work
            if self.single_job:
                self.jobs.append(Job(self.start_time, self.end_time, self.work1))
            # -> work, work
            else:
                midtime = self.start_time + (self.end_time - self.start_time)/2
                midtime = Day._validate_time(":".join([str(midtime.hour), str(midtime.minute)]), self.date)

                self.jobs.append(Job(self.start_time, midtime, self.work1))
                self.jobs.append(Job(midtime, self.end_time, self.work2))

    def _validate_work(self, work_str: str):
        elements = [element.strip() for element in work_str.split(";")][0:5]

        if len(elements) == 1 and elements[0].lower() in ["dzień wolny", "dzien wolny", "freeday", "urlop"]:
            self.is_free_day = True
            return elements[0]
        # if 4 elements provided and all are nonempty string
        elif len(elements) == 4 and all(element for element in elements):
            return elements
        else:
            return None

    @staticmethod
    def _validate_time(time_str: str, forced_date: datetime.date) -> datetime.datetime:
        """
        Validate time in XX:XX format.
        Return None if fail.
        """
        # remove all characters except for digits and ":"
        time_str = ''.join(c for c in time_str if c in "0123456789:")

        h_m_list = time_str.split(":")
        if not len(h_m_list) >= 2: return None

        h, m = [int(val) for val in h_m_list[:2]]

        # solve hours
        is_next_day = not (h % 24 == h)
        if is_next_day: h -= 24

        # solve minutes
        if m > 59: return None

        # round, and fix 58 and 59 rounding to 60
        m = int(5 * round(float(m) / 5))
        if m == 60: m = 55

        # format to XX:XX
        h_str = str(h)
        if len(h_str) < 2: h_str = "0" + h_str
        m_str = str(m)
        if len(m_str) < 2: m_str = "0" + m_str

        time = as_time(h_str + ":" + m_str)

        # add day if needed
        if is_next_day: forced_date += datetime.timedelta(days=1)

        # return combined
        return datetime.datetime.combine(forced_date, time)



class Month:
    def __init__(self, name, sheetData):
        self.days = []
        self.name = name

        # look for day data in 31 rows
        for row in sheetData[:32]:
            # Limit row to 8 columns
            row = row[:8]

            # remove trailing empty string values
            for i, value in reversed(list(enumerate(row))):
                clipAt = i+1
                if value != "":
                    break
            row = row[:clipAt]

            # Skip if row doesn't contain day data OR less then 7 columns provided
            if not (len(row) > 0 and is_date_string(row[0])) or len(row) < 7:
                continue

            # If 7 columns provided, add empty one, so there is always 8 columns provided
            if len(row) == 7:
                row.append("")

            # limit columns A B C D E G H (no column F)
            del row[5]

            self.days.append(Day(row))

    def get_valid_days(self):
        return [day for day in self.days]


def get_months(spreadsheet_id):
    # Collect worksheets names
    names = [sheet['properties']['title'] for sheet in sheetsapi.get_worksheets(spreadsheet_id)]

    # Collect all worksheets is spreadsheet
    worksheets = sheetsapi.get_ranges_batch(spreadsheet_id, ranges=names)

    # Determine if sheet has month data, exclude if not.
    # If cell A1 contains date string, sheet is valid for collection.
    worksheets = [worksheet for worksheet in worksheets if is_date_string(worksheet['values'][0][0])]

    months = [Month(
        # get name from range
        ws['range'].split("!")[0],
        ws['values'])
        for ws in worksheets]

    return months






def as_time(time_str):
    return datetime.datetime.strptime(time_str, "%H:%M").time()


# def is_time_string(time_str):
#     try:
#         time = as_time(time_str)
#     except:
#         time = None
#
#     return isinstance(time, datetime.time)


def as_date(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()


def is_date_string(date_str):
    try:
        date = as_date(date_str)
    except:
        date = None

    return isinstance(date, datetime.date)
