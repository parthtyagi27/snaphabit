import icalendar
import sys
import os
import arrow
import datetime

input_file_path = ""
shift_inital_date = ""
output_file = ""

def main():
    if len(sys.argv) < 3:
        print("Not enough arguments specified")
        print("Specify relative input file in the first parameter (./testCalendar.ics)")
        print("Specify start date in the second parameter (6/14)")
        return
    input_file_path = os.path.abspath(sys.argv[1])
    shift_inital_date = sys.argv[2]
    if len(sys.argv) == 3:
        output_file = "out.ics"
    else:
        output_file = sys.argv[3]

    # Loaded inputs and determined output file name

    input_calendar = icalendar.Calendar.from_ical(open(input_file_path, "rb").read())
    # print(input_calendar)
    counter = 0
    init_shift = 0
    shift_date = datetime.date(datetime.datetime.today().year, int(shift_inital_date.split("/")[0]), int(shift_inital_date.split("/")[1]))

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
            start = start.replace(day=int(shift_inital_date.split("/")[1]))
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

    output = open(os.path.abspath(output_file), "wb+")
    output.write(input_calendar.to_ical())
    output.close()




if __name__ == "__main__":
    main()