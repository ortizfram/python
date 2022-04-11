def greeting(name):
    print("welcome, " + name)

greeting("Franco")
greeting("valentina")

def greeting2(name, department):
    print("Welcome, "+ name)
    print("you are part of "+ department)

greeting2("Franco", "IT support")

#----------function// print_seconds function so that it prints the total amount of seconds
# given the hours, minutes, and seconds function parameters. Remember that there are 3600 seconds in an hour and 60 seconds in a minute.

def print_seconds(hours, minutes, seconds):
    hours *= 3600
    minutes *= 60
    print(hours+minutes+seconds)
print_seconds(1,2,3)


#-----------RETURNING VALUES
#Use the get_seconds function to work out the amount
# of seconds in 2 hours and 30 minutes, then add this
# number to the amount of seconds in 45 minutes and 15 seconds. Then print the result.
def get_seconds(hours, minutes, seconds):
    return 3600*hours + 60*minutes + seconds #return: to define a default opp to aplly certain number
    # of times in the code

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)


#----------luckyNumberFunction
def luckyNumber(name):
    number = len(name) * 9
    print("Hello " + name + " your lucky number is: " + str(number))
luckyNumber("Franco")      #you may put the name of the function not the variable
luckyNumber("Henrique")    #it makes the script shorter


#-----------reduce the code duplication in the script
# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
# receives the name of the month and the number of days in that month as parameters. Adapt the rest of
# the code so that the result is the same. Confirm your results by making a function call with the
# correct parameters for both months listed.
#////
# june_days = 30
# print("June has " + str(june_days) + " days.")
# july_days = 31
# print("July has " + str(july_days) + " days.")
# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
def month_days(month, days):
    print(month + " has " + days + " days.")
month_days("june","30")
month_days("july", "31")


#---------REFACTORING--(make it pretty)***///
# def calculate(d):
#     q = 3.14
#     z = q * (d**2)
#     print(z)
# calculate(5)
def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)
circle_area(5)

#---//2--------
# def f1(x, y):
# 	z = x*y  # the area is base*height
# 	print("The area is " + str(z))
def rectangle_area(base, height):
    area = base * height
    print("The area is "+ str(area))
rectangle_area(5, 6)


#----1QUIZ
# This function converts miles to kilometers (km).
# Complete the function to return the result of the conversion
# Call the function to convert the trip distance from miles to kilometers
# Fill in the blank to print the result of the conversion
# Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
    return miles * 1.6
my_trip_miles = 55
# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(55)
# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))
# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str((my_trip_km)**2))


#-----2QUIZ (increased order of numbers)
# This function compares two numbers and returns them in increasing order.
# Fill in the blanks, so the print statement displays the result of the function call in order.
# Hint: if a function returns multiple values, don't forget to store these values in multiple variables

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1
# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)


#-----3QUIZ (lucky_number_return_text)
# Let's revisit our lucky_number function. We want to change it, ' \
#    'so that instead of printing the message, it returns the message. ' \
#    'This way, the calling line can print the message, or do something ' \
#    'else with it if needed. Fill in the blanks to complete the code to make it work.

def lucky_number(name):
    number = len(name) * 9
    lucky = "Hello " + name + ". Your lucky number is " + str(number)
    return lucky
print(lucky_number("Kay"))
print(lucky_number("Cameron"))