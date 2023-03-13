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