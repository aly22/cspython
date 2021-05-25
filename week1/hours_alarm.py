time_now=int(input("Please enter the time now: "))
alarm=int(input("Please enter when the alarm should go off: "))
alarm_goes_off=time_now+(alarm%24)
print("The alarm goes off this time:",alarm_goes_off)