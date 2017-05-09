import gsheets_data_parser
import gui

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
    # months = gsheets_data_parser.get_months(settings['spreadsheetId'])
    #gui.update??
    # gui.update()



def main():
    gui.startApp()
    refresh()
    # tests()

if __name__ == '__main__':
    main()
