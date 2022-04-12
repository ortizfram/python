print(10>1) #//boolean
print("cat" == "dog")
print (1 !=  2)
#print (1 < "1")  #int & string  #comparing if bigger cant be done
print(1 == "1")  #different = true

#-----UPPER CASE (smaller thar lower case)


#-----LOGICAL OPPERATORS (and, or, not)
print ("---")
print(1<2 and 2 == 3) #and both true to true
print(25 > 50 or 1 != 2) #true when 1 of 2, false when bouth false
print(not 42 == "answer") #its like the ! before in java (it turns it true or false)

print("--is positive-")
#----Function Valid username
def hint_username(username):
    if len(username) < 3:
        print("Invalid. Must be at least 3 chars")

#-----Function Possitive Number
# should return True if
# the number received is positive, otherwise
# it returns None. Can you fill in the gaps to make
# that happen?
def is_positive(number):
    if (number > 0):
        print("true")
        return True
    else:
        print("false")
        return False
is_positive(-1)

print("---is even")
#-------Function is even
def is_even(number):
    if number % 2 == 0:
        print("true")
        return True
    print("false")
    return False
is_even(3)

#------Funtion no longer than 15
def hint_username(username):
    if len(username) < 3:
        print("Invalid. Must be at least 3 chars")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 chars")
    else:
        print("valid username")

print("---group numb")
#-----number_group function
def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative


print("---if not Taylor")
#-----if not Taylor send greetings
def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  elif name != "Taylor":
      return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))


print("--if equals 10")
#--- if number equals 10
def if_number_is_ten(number):
   if number >= 20 or number < 12:
      print(2)
   else:
       print(3)

if_number_is_ten(10)


print("---calculate storage")
#--------Funct calculate storage
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return block_size * full_blocks + block_size
    return block_size * full_blocks

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192