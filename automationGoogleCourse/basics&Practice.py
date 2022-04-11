#----------LIST
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)

#----------RANGE
for i in range(3):
    print ("hello world")

#----------CALCULATE
a= (((1+2)*3)/4)**5
print (a)

#-----------RAIZ(ratio)
ratio= (1+(5**(1/2)))/2
print("ratio = ", ratio)

#-----------SecondInWeek
day = 86400 #seconds
print(day*7)

#----------PossiblePasswordAmountInLower
oneLetter = 26
number = 6
if (number <= 6):
    print("if pass is 6 letters:")
    print("possibilities are: ", number**26)

#----------sectorsOfADisk
# Most hard drives are divided into sectors
# of 512 bytes each.  Our disk has a
# size of 16 GB. Fill in the blank to
# calculate how many sectors the disk has.

disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = (((16*1024*1024*1024)/512))

print(sector_amount)



#--Str()---------CONVERT.EXPRESSIONS_AverageSizes
total = 2048 + 4357 + 97658 + 125 + 8
files = 5   #explicit Converion: manually #Implicit: automatically
average = total / files
print("The average size is: " + str(average))

#----------------sharingBill + Tip
bill = 47.28
tip = bill * 0.15
total = bill + tip
share = total/2
print("Each person needs to pay: "+ str(share))#int to float


#---------------fixTheError//// the result is equal to 1, and display
# the result on the screen. Unfortunately, there
# is an error in the code. Find the error and fix it, so that the output is correct.
#//////
# #numerator = 10
# denominator = 0
# result = numerator / denominator
# print(result)

numerator = 10
denominator = 0
result = (numerator / denominator) if denominator != 0 else 1
print(result)

#-----------combiningVariables
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(word1+ " " + word2 + " " + word3 + " " + word4 + " " + word5+ " " + word6+ " " + word7)

#-----------fixTheOutput// is supposed to display "2 + 2 = 4"
#print("2 + 2 = " + (2 + 2))
print("2 + 2 = " + str(2 + 2))







