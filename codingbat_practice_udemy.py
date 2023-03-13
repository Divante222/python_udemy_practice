# The parameter weekday is True if it is a weekday, 
# and the parameter vacation is True if we are on vacation. 
# We sleep in if it is not a weekday or we're on vacation. 
# Return True if we sleep in.


def sleep_in(weekday, vacation):
  if weekday == False and vacation == True:
    return True
  elif weekday == True and vacation == False:
    return False
  elif weekday == False and vacation == True:
    return True
  elif weekday == False and vacation == False:
    return True
  elif weekday == True and vacation == True:
    return True
  
# We have two monkeys, a and b, and the parameters a_smile 
# and b_smile indicate if each is smiling. We are in trouble 
# if they are both smiling or if neither of them is smiling. 
# Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
  if a_smile == True and b_smile == True:
    return True
  elif a_smile == False and b_smile == False:
    return True
  elif a_smile == True and b_smile == False:
    return False
  elif a_smile == False and b_smile == True:
    return False


# Given two int values, return their sum. Unless the two values 
# are the same, then return double their sum.

def sum_double(a, b):
  if a == b:
    return (a+b) * 2
  elif a != b:
    return a + b

# Given an int n, return the absolute difference between n 
# and 21, except return double the absolute difference if n 
# is over 21.

def diff21(n):
  if n > 21:
    return (n - 21) * 2
  elif n < 21:
    return 21 - n
  elif n == 21:
    return 0
  
# We have a loud talking parrot. The "hour" parameter 
# is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour 
# is before 7 or after 20. Return True if we are in trouble.

def parrot_trouble(talking, hour):
  if talking == True and hour < 7 or talking == True and hour > 20:
    return True
  elif talking == True and hour > 7 or talking == True and hour < 20:
    return False
  elif talking == False and hour > 20 or talking == False and hour < 7:
    return False
  elif talking == False and hour > 7 or talking == False and hour < 20:
    return False
  
#   Given 2 ints, a and b, return True if one if them is 10 or 
#   if their sum is 10.

def makes10(a, b):
  if a == 10 or b == 10:
    return True
  elif a + b == 10:
    return True
  else:
    return False
  
# Given an int n, return True if it is within 10 of 100 or 200. 
# Note: abs(num) computes the absolute value of a number.

def near_hundred(n):
  if n < 111 and n > 89:
    return True
  elif n < 211 and n > 189:
    return True
  else:
    return False
  
# Given 2 int values, return True if one is negative and 
# one is positive. Except if the parameter "negative" is True, 
# then return True only if both are negative.

def pos_neg(a, b, negative):
  if a < 0 and b < 0 and negative == True:
    return True
  elif a > 0 and b < 0 and negative == False:
    return True
  elif a < 0 and b > 0 and negative == False:
    return True
  elif a > 0 and b > 0 and negative == False:
    return False
  elif a < 0 and b < 0 and negative == False:
    return False
  elif a < 0 and b > 0 and negative == True:
    return False
  elif a > 0 and b > 0 and negative == True:
    return False
  elif a > 0 and b < 0 and negative == True:
    return False
  
# Given a string, return a new string where "not " has been added 
# to the front. However, if the string already begins with "not", 
# return the string unchanged.

def not_string(str):
  if str[0:3] != 'not':
    return 'not ' + str
  elif str[0:3] == 'not':
    return str