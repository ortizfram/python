print ("#introduction"+"\n")
x=0
while x<5:
    print("not there yet, x= "+str(x))
    x = x+1
print("x="+ str(x))
print("\n")
############################
print("#2"+"\n")
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
attempts(5)
print("\n")
##############################
print("#3"+"\n")
my_variable =5
while my_variable < 10:
    print("hi")
    my_variable +=1
print("\n")
    ######################
print("#4"+"\n")
def count_down(start_number):
    current = 3
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")

count_down(3)