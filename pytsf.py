import datetime

import cmd_questions
import filler
import gsheets_data_parser

settings = {"name": "Paweł Grzelak",
            "spreadsheetId": "1jXygiAnEQ-BzK7ZMkduJMA0QETZ2_-8IE-jUQsmZ7-4"}


def tests():
    day = gsheets_data_parser.Day(["2017-05-24", "10:20", "13:00", "13:30", "17:59", "xxxxxx", "xxxxxx"])
    filler.fill_day(day)
    pass



def main():
    """ Update data, refresh gui """
    start = datetime.datetime.now()
    months = gsheets_data_parser.get_months(settings['spreadsheetId'])
    print("\n\n----------------\nCzas ściągania danych: {0}".format(datetime.datetime.now() - start) + "\n----------------")
    cmd_questions.ask(months)


if __name__ == '__main__':
    # gui.startApp()
    # main()
    tests()
