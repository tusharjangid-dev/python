import time 

hour = int(input("Enter the hour (0-23): "))

for i in range(1):
    if hour < 12:
        print("Good Morning")
    elif hour < 17:
        print("Good Afternoon")
    elif hour < 21:
        print("Good Evening")
    elif hour < 24:
        print("Good Night")
    else:
        print("Please enter a valid hour between 0 and 23 ")

    print("------------------------------")


print(time.strftime("But Current Time is: %d-%m-%Y %H:%M:%S"))
