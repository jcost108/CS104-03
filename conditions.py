#initialize variable
temp = 0

print("\nWeather Conditions Checker")
print("Enter temperature to recieve clothing recommendation.")
print("To terminate program, input 999.\n")

#while loop allows program to repeat
while temp != 999:

    #ask user for temperature
    temp = int(input("Please enter the current outside temperature: "))

    if temp == 999:
        break

    elif temp > 90:
        print("Wear shorts.\n")

    elif temp > 70:
        print("Short sleeves are fine.\n")

    elif temp > 50:
        print("Wear a jacket.\n")

    elif temp > 32:
        print("Wear a heavy coat.\n")

    else:
        print("Stay inside.\n")

print("Goodbye.")
