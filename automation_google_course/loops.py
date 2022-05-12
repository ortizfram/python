print("#introduction" + "\n")
x = 0
while x < 5:
    print("not there yet, x= " + str(x))
    x = x + 1
print("x=" + str(x))
print("\n")
############################################################
print("#2" + "\n")


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")


attempts(5)
print("\n")
############################################################
print("#3" + "\n")
my_variable = 5
while my_variable < 10:
    print("hi")
    my_variable += 1
print("\n")
############################################################
print("#4" + "\n")


def count_down(start_number):
    current = 3
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")


count_down(3)

print("\n")
############################################################
print("#5" + "\n")


# INFINITE LOOP///
def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n <= end:
        print(n)
        n += 1


print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)
print("\n")

############################################################
print("#6" + "\n")


def print_prime_factors(number):
    # Start with two, which is the first prime
    factor = 2
    # Keep going until the factor is larger than the number
    while factor <= number:
        # Check if factor is a divisor of number
        if number % factor == 0:
            # If it is, print it and divide the original number
            print(factor)
            number = number / factor
        else:
            # If it's not, increment the factor by one
            factor += 1
    return "Done"


print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT
print("\n")
############################################################
print("7" + "\n")


# SUM DIVISOR TILL BEFORE N ///
def sum_divisors(n):
    sum = 0
    i = 1
    while i <= n / 2:
        if (n % i == 0):  # if reminder of division = 0, add + number and print
            sum = sum + i
            print(str(i) + "+")  # just shows number you can divide and +
        i += 1  # upgrade possible numbers s
    return sum
    # Return the sum of all divisors of n, not including n


print(sum_divisors(0))
# 0
print("\n")
print(sum_divisors(3))  # Should sum of 1
# 1
print("\n")
print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# 55
print("\n")
print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51
# 114
print("\n")

##########################################################################3
print("8" + "\n")


def multiplication_table(number):
    # Initialize the starting point of the multiplication table
    multiplier = 1
    # Only want to loop through 5
    while multiplier <= 5:
        result = number * multiplier
        # What is the additional condition to exit out of the loop?
        if result >= 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the variable for the loop
        multiplier += 1


multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15
print("\n")

multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25
print("\n")

multiplication_table(8)
# Should print: 8x1=8 8x2=16 8x3=24
print("\n")
######################################################################################
# FOR LOOP///
#####################################################################################
print("\n")
print("#for 2 sum squares" + "\n")


def square(n):
    return n * n


def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += int(square(n))  # 1+4+9+16+25+36+49+64+81(not 10*10) = 285
    return sum


print(sum_squares(10))  # Should be 285
print("\n")
##########################################################################################
print("#for 3/ average from tupple FOR" + "\n")
values = [23, 54, 66, 3, 90]
sum = 0
length = 0
for value in values:
    sum += value
    length = +1
print("SUm= " + str(sum) + " -average = " + (str(sum / length)))
print("\n")
#####################################################################3#
print("#2 for: factorial of 4 & 5" + "\n")


def factorial(n):  # its a num that * with next x, till original n
    result = 1
    for x in range(1, n + 1):
        result = result * x
    return result


print("factorial 4: " + str(factorial(4)))  # should return 24
# 1*1 =1*2 =2*3 =6*4 =[24]
print("factorial 5: " + str(factorial(5)))  # should return 120
print("\n")
###################################################################3
print("#for 3 PARAMETRES")
for x in range(0, 101, 10):  # 2nd is couse goes till number -1
    # 3th number increments by 10
    # 1st couse is from 0
    print(x)
print("\n")
####################################################################
# NESTED FOR LOOPS
####################################################################
print("#1 nested for loop" + "\n")
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()
print("\n")
###################################################################
print("#2 nested for loop"+"\n")
teams = ["9z", "furios", "movistar", "sharks"]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team+" vs "+away_team)
print("\n")
###################################################################
print("#3 nested for loop"+"\n")
#multiples of 7 between 0 and 100.
def multiples(x):
    for n in range(100):
        n = (n*x)
        if n <= 100:
            print(n)
print(multiples(7))
