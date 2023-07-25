exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

stat = ''

if exam_hour < arrival_hour:
    stat = 'Late'
    diff_hour = arrival_hour - exam_hour
    lateness_min = arrival_minute + (60 - exam_minute)
    if exam_minute > arrival_minute:
        diff_hour = diff_hour - 1
    if lateness_min > 59:
        lateness_min -= 60
    print(stat)
    if diff_hour > 0:
        print(f'{diff_hour}:{lateness_min:02d} hours after the start')
    else:
        print(f'{lateness_min} minutes after the start')
elif exam_hour == arrival_hour:
    diff_minute = abs(exam_minute - arrival_minute)
    if (exam_minute > arrival_minute and diff_minute <= 30) or diff_minute == 0:
        stat = 'On time'
        print(stat)
        if diff_minute > 0:
            print(f'{diff_minute} minutes before the start')
    elif exam_minute < arrival_minute:
        stat = 'Late'
        print(stat)
        print(f'{diff_minute} minutes after the start')
    elif exam_minute > arrival_minute:
        stat = 'Early'
        print(stat)
        print(f'{diff_minute} minutes before the start')
elif exam_hour > arrival_hour:
    early_min = exam_minute + (60 - arrival_minute)
    if early_min > 30:
        stat = 'Early'
    else:
        stat = 'On time'
    diff_hour = exam_hour - arrival_hour
    if arrival_minute > exam_minute:
        diff_hour -= 1
    if early_min > 59:
        early_min -= 60
    print(stat)
    if diff_hour > 0:
        print(f'{diff_hour}:{early_min:02d} hours before the start')
    else:
        print(f'{early_min} minutes before the start')
