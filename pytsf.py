import sheetsapi
from datetime import date, time, datetime




# time validator clsss which accepts hours above 24, and marks them as "next day"
class TimeVal:
    def __init__(self, timeStr):
        # datetime.strptime(self.startTime, "%H:%M").time()
        pass

    def is_next_day(self):
        pass


class Day:
    def __init__(self, values):
        self.date = values[0]
        self.startTime = values[1]
        self.startLunch = values[2]
        self.endLunch = values[3]
        self.endTime = values[4]
        self.validate()


    def _timeValidate(self, timeStr):
        pass

    def validate(self):
        # date validation
        self.date = datetime.strptime(self.date, "%Y-%m-%d").date()

        # startTime validation
        self.startTime = TimeVal(self.startTime)


        print("Day--->", self.date, self.startTime, self.startLunch, self.endLunch, self.endTime)



def orderAsMonth(valueRanges):
    # DayOfMonth = namedtuple("DayOfMonth", ["date", "startTime", "startLunch", "endLunch", "endTime"])

    values = [range.get("values", [[""]])[0][0] for range in valueRanges]
    valuesForEachDay = [values[x:x+5] for x in range(0, len(values), 5)]

    # ommit non existent days (for example 31st day in 30 days long month)
    days = [ (Day(dayValues)) for dayValues in valuesForEachDay if len(dayValues[0]) != 0]


def main():
    ranges = [(col + str(day)) for day in range(1, 32) for col in ["A", "B", "C", "D", "E"]]
    valueRanges = sheetsapi.getValueRanges(ranges)
    orderAsMonth(valueRanges)


if __name__ == '__main__':
    main()