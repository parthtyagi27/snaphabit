import ics
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

    input_calendar = ics.Calendar(open(input_file_path).read())
    print(input_calendar.events)

    output_calendar = ics.Calendar()

    shift_arrow = arrow.get(int(arrow.utcnow().year), int(shift_inital_date.split("/")[0]), int(shift_inital_date.split("/")[1]))
    print(shift_arrow)

    # for event in input_calendar.timeline.__iter__():
    #     print("Shifting Event: ")
    #     print(event)
    #     diff_begin = shift_arrow - event.begin
    #     diff_end = shift_arrow - event.end
    #     hours,remainder = divmod(diff_begin.seconds,3600) # Get Hour 
    #     minutes,seconds = divmod(remainder,60) # Get Minute & Second 
    #     print(diff_begin.days)
    #     print(diff_end.days)
    #     print(event.begin.shift(days=diff_begin.days))
    #     print(event.end.shift(days=diff_end.days, seconds=diff_end.seconds))
    #     print("\n")
    counter = 0
    for event in input_calendar.timeline:
        print(event)
        if counter == 0:
            # First event -> set to shift date
            print("Begin = " + str(event.begin))
            print("End = " + str(event.end))
            duration = event.duration
            print(duration)
            event.end = event.end.shift(years=+1)
            print("Temp End = " + str(event.end))
            event.begin = event.begin.replace(month=int(shift_inital_date.split("/")[0]), day=int(shift_inital_date.split("/")[1]))
            print("Final begin" + str(event.begin))
            print(event.duration)
            event.end = event.begin + event.duration
            print("Temp end " + str(event.end))
            event.end = event.end.shift(years=-1)
            print("Final end" + str(event.end))
            print("SHIFTED")
            # print(event)
        print("\n")
        counter += 1

    print(counter)



if __name__ == "__main__":
    main()