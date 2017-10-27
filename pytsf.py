import datetime

import cmd_questions
import filler
import gsheets_data_parser
from settings import Settings

# todo: Load settings from file
settings = {"name": "Paweł Grzelak",
            "spreadsheetId": "1jXygiAnEQ-BzK7ZMkduJMA0QETZ2_-8IE-jUQsmZ7-4"}


def tests():
    # day1 = gsheets_data_parser.Day(["2017-05-24", "9:20", "13:00", "13:30", "18:00", "Przemysław Stopa;Przemkowe;Przemysław Stopa;Przemkowe", ""])

    months = gsheets_data_parser.get_months(settings['spreadsheetId'])
    filler.fill(months, 0, [24])


def main():
    print("\n\nŚciągam dane z googli, czekaj...")
    start = datetime.datetime.now()
    months = gsheets_data_parser.get_months(settings['spreadsheetId'])
    print("----------------\nCzas ściągania danych: {0}".format(datetime.datetime.now() - start) + "\n----------------")
    cmd_questions.ask(months)


if __name__ == '__main__':
    Settings.load()
    # main()
    tests()
