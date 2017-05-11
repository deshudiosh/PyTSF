import form_filler


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
    ranges_str_list = "".join([char for char in ranges_str if char in "0123456789,-"]).split(",")
    ranges = []
    for rng in ranges_str_list:
        if "-" in rng:
            vals = rng.split("-")
            if len(vals) == 2 and vals[0] < vals[1]:
                ranges += [i for i in range( int(vals[0]), int(vals[1])+1 )]
        else:
            ranges.append(int(rng))

    return sorted(ranges)

def _ask_days(months, month_idx):
    month = months[month_idx]
    print("\nPoprawnie wypełnione dni w ({0}):".format(month.name))
    print([day.date.day for day in month.get_valid_days()])

    while True:
        print("\nWpisz które chcesz wypełnić. Np: 1, 2, 6, 12, 20-30.\nNapisz X aby cofnąć do wyboru miesiąca.")
        days_str = str(input())

        if days_str == "x":
            _ask_month(months)
            return
        else:
            days = _get_int_ranges(days_str)
            if len(days) >= 1:
                break

    print("\nTe dni będą wypelnione:")
    print(days)
    form_filler.fill(months, month_idx, days)

def ask(months):
    print("""

    Siemasz cwelu!
    Ten wyjebisty sofcik napisał Grzelak. 
    Wisisz stówkę.

    """)

    _ask_month(months)





