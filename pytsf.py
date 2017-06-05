import datetime

import cmd_questions
import filler
import gsheets_data_parser

# todo: Load settings from file
settings = {"name": "Paweł Grzelak",
            "spreadsheetId": "1jXygiAnEQ-BzK7ZMkduJMA0QETZ2_-8IE-jUQsmZ7-4"}


def tests():
    day1 = gsheets_data_parser.Day(["2017-05-24", "9:20", "13:00", "13:30", "18:00", "Przemysław Stopa;Przemkowe;Przemysław Stopa;Przemkowe", ""])
    day2 = gsheets_data_parser.Day(["2017-05-24", "10:20", "", "", "17:59", "Przemysław Stopa;Przemkowe;Przemysław Stopa;Przemkowe", ""])
    day3 = gsheets_data_parser.Day(["2017-05-24", "10:20", "", "", "17:59", "Przemysław Stopa;Przemkowe;Przemysław Stopa;Przemkowe", "MSD;MSD;Adam Urbaniak;MSD"])
    day4 = gsheets_data_parser.Day(["2017-05-24", "9:20", "13:00", "13:30", "17:59", "Dzień wolny", ""])
    # filler.fill_days([day1, day2, day3, day4])
    filler.fill_days([day1])


def main():
    """ Update data, refresh gui """
    start = datetime.datetime.now()
    months = gsheets_data_parser.get_months(settings['spreadsheetId'])
    print("\n\n----------------\nCzas ściągania danych: {0}".format(datetime.datetime.now() - start) + "\n----------------")
    cmd_questions.ask(months)


if __name__ == '__main__':
    main()
    # tests()
