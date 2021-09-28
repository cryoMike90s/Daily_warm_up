from datetime import datetime

def day_difference(two_dates):
    _daty = []
    for date in two_dates:
        date = datetime.strptime(date, '%d/%m/%Y').date()
        _daty.append(date)
    difference = abs((_daty[0] - _daty[1]).days)
    return print("Between {} and {} there are {} days difference".format(_daty[0],_daty[1], difference))



two_dates = ['24/07/2021', '21/07/2021']
day_difference(two_dates)