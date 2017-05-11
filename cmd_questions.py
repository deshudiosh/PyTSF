def _ask_month(months):

    numbered_month_names = []
    for i in range(len(months)):
        numbered_month_names.append('[%x]' % (i+1) + months[i].name)

    print('Który miesiąc? Wpisz cyfrę i Enter')

    chosen = -1
    while chosen == -1:
        print("  ".join(numbered_month_names))
        num = int(input())

        if num >= 1 and num <= len(months):
            chosen = num - 1
        else:
            print("--> Napisz tylko numer miesiąca pało")

    print("Wybrałeś ({0})".format(months[chosen].name))

    _ask_days(months, chosen)

def _get_int_ranges(ranges_str):
    days_str = [char for char in days_str if char in "0123456789,-"]
    return ["no kurwa, co to"]

def _ask_days(months, month_idx):
    month = months[month_idx]
    print("\nPoprawnie wypełnione dni w ({0}):".format(month.name))
    print([day.date.day for day in month.get_valid_days()])
    print("\nWpisz które chcesz wypełnić. Np: 1, 2, 6, 12, 20-30.\nNapisz X aby cofnąć do wyboru miesiąca.")
    days_str = str(input())

    if days_str == "x":
        _ask_month(months)
        return

    print(_get_int_ranges(days_str))


def ask(months):
    print("""

    Siemasz cwelu!
    Ten wyjebisty sofcik napisał Grzelak. 
    Wisisz stówkę.

    """)
    _ask_month(months)




