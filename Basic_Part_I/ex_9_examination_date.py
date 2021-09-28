from datetime import datetime


def examination_schedule(data):
    data_first = datetime(*data).date()
    data_ex = data_first.strftime("%d-%m-%Y")
    return print("The examination starts from {}".format(data_ex))


data = (2014, 11, 12)
examination_schedule(data)