from num2words import num2words
from datetime import datetime

def str_to_datetime(date_str, time_str):
    date = datetime.strptime(date_str.strip(), '%d.%m.%Y').date()
    time = datetime.strptime(time_str.strip(), '%H:%M').time()
    return date, time


def insert_all_dates(num):
    dates = []
    times = []
    for i in range(num):
        date_str = input("Please enter a date (DD.MM.YYY): ")        
        time_str = input("Please enter a time (HH:MM): ")
        date, time = str_to_datetime(date_str, time_str)
        dates.append(date)
        times.append(time)
    
    return dates, times


def check_datetime_reached(date, time):
    now = datetime.now()
    if now >= datetime.combine(date, time):
        return True
    return False


def print_result(num, dates, times):
    for i in range(num):
        ordinal = num2words(i+1, to='ordinal')
        if check_datetime_reached(dates[i], times[i]):
            print("The {} date has been reached! ({} - {})"\
                .format(ordinal, dates[i].strftime('%d.%m.%Y'), \
                        times[i].strftime('%H:%M')))
        else:
            print("The {} date has not been reached! ({} - {})"\
                    .format(ordinal, dates[i], times[i]))



if __name__ == "__main__":
    num = int(input("How many data do you want to enter? \t"))
    dates, times = insert_all_dates(num)
    
    print("Thank you very much. I will notify you!")
    print("...")

    print_result(num, dates, times)

