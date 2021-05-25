day1 = int(input("Please enter the starting day number: "))
length_of_stay = int(input("Please enter the length of your stay: "))
leave_day =day1+length_of_stay%7
print("The leaving day will be: ",leave_day)
