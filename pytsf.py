import datetime

import gsheets_data_parser
import sheetsapi

settings = {"name": "Paweł Grzelak",
            "spreadsheetId": "1jXygiAnEQ-BzK7ZMkduJMA0QETZ2_-8IE-jUQsmZ7-4"}



def tests():
    # testday = ["2017-04-03", '11:00', '0', '0', '18:30', '7:30', 'Przemysław Stopa;Przemkowe;Przemysław Stopa;Przemkowe']
    # gsheets_data_parser.Day(testday)

    test_hours = ["text", "", "j 12:00 ec", "00:00", "00:09",
                  "", "12:00", "12:12", "12:13:12", "12:59", "12:68", "23:00", "24:00", "24:20", "27:50"]

    for h in test_hours:
        somedate = gsheets_data_parser.as_date("2017-05-22")
        print(h, " -> ", gsheets_data_parser.validate_time(h, somedate))



def refresh():
    """ Update data, refresh gui """
    months = gsheets_data_parser.getMonths(settings['spreadsheetId'])
    #gui.update??



def main():
    refresh()
    # tests()

if __name__ == '__main__':
    main()














######################################
# OLD JUNK YAHA

# class Day:
#     def __init__(self, values):
#         self.date = values[0]
#         self.startTime = values[1]
#         self.startLunch = values[2]
#         self.endLunch = values[3]
#         self.endTime = values[4]
#         self.validate()
#
#
#     def _timeValidate(self, timeStr):
#         pass
#
#     def validate(self):
#         # date validation
#         self.date = datetime.strptime(self.date, "%Y-%m-%d").date()
#
#         # startTime validation
#         #self.startTime = TimeVal(self.startTime)
#
#
#         print("Day--->", self.date, self.startTime, self.startLunch, self.endLunch, self.endTime)
#
#
#
# def orderAsMonth(valueRanges):
#     # DayOfMonth = namedtuple("DayOfMonth", ["date", "startTime", "startLunch", "endLunch", "endTime"])
#
#     values = [range.get("values", [[""]])[0][0] for range in valueRanges]
#     valuesForEachDay = [values[x:x+5] for x in range(0, len(values), 5)]
#
#     # ommit non existent days (for example 31st day in 30 days long month)
#     days = [ (Day(dayValues)) for dayValues in valuesForEachDay if len(dayValues[0]) != 0]
#
#
# def main():
#     ranges = [(col + str(day)) for day in range(1, 32) for col in ["A", "B", "C", "D", "E"]]
#     #valueRanges = sheetsapi.getValueRanges(ranges)
#     #orderAsMonth(valueRanges)





