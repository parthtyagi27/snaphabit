import icalendar
import sys
import os
import datetime

def shiftFile(input_file, shift_input):
    input_calendar = icalendar.Calendar.from_ical(input_file.read())
    print(input_calendar)
    counter = 0
    init_shift = 0
    shift_date = datetime.date(datetime.datetime.today().year, int(shift_input.split("-")[1]), int(shift_input.split("-")[2]))

    for event in input_calendar.walk("vevent"):
        # init = datetime
        if counter == 0:
            start = event['dtstart'].dt
            end = event['dtend'].dt
            duration = end - start
            init_shift = shift_date - start.date()
            print("Start = " + str(start))
            print("End = " + str(end))
            print("Duration = " + str(duration))
            print("Init shift = " + str(init_shift))
            start = start.replace(day=int(shift_input.split("-")[2]))
            end = start + duration 
            print(start)
            print(end)
            event['dtstart'].dt = start
            end = event['dtend'].dt = end
        else:
            # Shift relative to first event
            start = event['dtstart'].dt
            end = event['dtend'].dt
            duration = end - start
            print("Start = " + str(start))
            print("End = " + str(end))
            print("Duration = " + str(duration))
            start = start + init_shift
            end = start + duration 
            print(start)
            print(end)
            event['dtstart'].dt = start
            end = event['dtend'].dt = end
            
        counter += 1
        print("\n")
    print("Events = " + str(counter))
    return input_calendar.to_ical()
    # output = open(os.path.abspath(output_file), "wb+")
    # output.write(input_calendar.to_ical())
    # output.close()