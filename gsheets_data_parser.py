import datetime

import sheetsapi

class Day:
    def __init__(self, rowData):
        """ Unpack row data to properties, BUT omit 6th column """
        del rowData[5]
        self.date, \
        self.start_time, \
        self.start_lunch, \
        self.end_lunch, \
        self.end_time, \
        self.work1 = rowData[:6]
        # there may be no work2 provided
        self.work2 = rowData[6] if len(rowData) >= 7 else None
        self._validate()

    def _validate(self):
        self.date = as_date(self.date)

        self.start_time = validate_time(self.start_time, self.date)
        self.start_lunch = validate_time(self.start_lunch, self.date)
        self.end_lunch = validate_time(self.end_lunch, self.date)
        self.end_time = validate_time(self.end_time, self.date)

        print(self.start_time, "-->", self.start_lunch, "-->", self.end_lunch, "-->", self.end_time)

        # TODO: CZEMU 6 stycznia jest brany pod uwage?
        # validate work1/2 somehow (num of elements?)
        # parse to Work class, containing properties (klient, osoba zlecajaca, itd)
        # assign "isValid" value!


class Month:
    def __init__(self, name, sheetData):
        self.days = []
        self.month_name = name
        # TODO: move all validation to Day class for readability
        for row in sheetData:
            # If first cell exists and contains date
            if len(row) > 0 and is_date_string(row[0]):
                # AND at least 6 columns of data provided
                if len(row) >= 7:
                    self.days.append(Day(row))


def get_months(spreadsheet_id):
    # Get worksheets
    worksheets = sheetsapi.get_worksheets(spreadsheet_id)

    # Collect worksheets names
    names = [sheet['properties']['title'] for sheet in worksheets]

    # Get data A1:H31 for each month (sheet name is valid A1 notation range too!)
    # TODO: Collect only needed cells
    # ranges = [(col + str(day)) for day in range(1, 32) for col in ["A", "B", "C", "D", "E"]]
    sheets_data = [sheetsapi.get_range_data(spreadsheet_id, name) for name in names]

    # Determine if sheet has month data.
    # If cell A1 contains date string, collect index of sheet (sheet is valid month data).
    valid_months_indexes = [index for index in range(len(sheets_data))
                            if is_date_string(sheets_data[index]['values'][0][0])]
    # Collect parsed months from valid sheets
    months = [Month(names[idx], sheets_data[idx]['values']) for idx in valid_months_indexes]

    return months


def validate_time(time_str: str, forced_date: datetime.date) -> datetime.datetime:
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
    m = int(5 * round(float(m)/5))
    if m == 60:m = 55


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


def as_time(time_str):
    return datetime.datetime.strptime(time_str, "%H:%M").time()


def is_time_string(time_str):
    try:
        time = as_time(time_str)
    except:
        time = None

    return isinstance(time, datetime.time)


def as_date(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()


def is_date_string(date_str):
    try:
        date = as_date(date_str)
    except:
        date = None

    return isinstance(date, datetime.date)
