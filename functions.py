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



