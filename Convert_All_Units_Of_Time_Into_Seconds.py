# Type your days, hours, minutes and seconds
Days = int(input("Input days: ")) * 3600 * 24
Hours = int(input("Input hours: ")) * 3600
Minutes = int(input("Input minutes: ")) * 60
Seconds = int(input("Input seconds: "))

Time = Days + Hours + Minutes + Seconds
print("The  amounts of seconds is: {}".format(Time))
