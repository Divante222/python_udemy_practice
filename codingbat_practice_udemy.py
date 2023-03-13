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
  
# Given a non-empty string and an int n, return a new string 
# where the char at index n has been removed. The value of n 
# will be a valid index of a char in the original string 
# (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str, n): 
  if n != 0:
    new_string = str[0:n] + str[n+1:]
    return new_string
  if n == 0:
    return str[n+1:]
  
# Given a string, return a new string where the first 
# and last chars have been exchanged.

def front_back(str):
  if len(str) == 1:
    return str
  elif len(str) == 2:
    return str[len(str) -1] + str[0]
  elif len(str) > 2:
    return str[len(str) -1] + str[1:len(str)-1] + str[0]
  else:
    return str
  
#   Given a string, we'll say that the front is the first 3 chars
#   of the string. If the string length is less than 3, the front 
#   is whatever is there. Return a new string which is 3 copies of 
#   the front.

def front3(str):
  if len(str) < 3:
    return str * 3
  else:
    return str[:3] * 3
  
# Given a string and a non-negative int n, return a larger 
# string that is n copies of the original string.

def string_times(str, n):
  return str * n

# Given a string and a non-negative int n, we'll say that the 
# front of the string is the first 3 chars, or whatever is there 
# if the string is less than length 3. Return n copies of the front;

def front_times(str, n):
  if len(str) < 3:
    return str * n
  else:
    return str[:3] * n
  
#   Given a string, return a new string made of every other char 
#   starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
  return str[::2]

# Given a non-empty string like "Code" return a 
# string like "CCoCodCode".

def string_splosion(str):
  new_string = ''
  for i in range(len(str)+1 ):
    new_string += str[:i]
    
  return new_string

# Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
  count = 0
  for i in nums:
    if i == 9:
      count+= 1
  return count

# Given an array of ints, return True if one of the first 
# 4 elements in the array is a 9. The array length may be 
# less than 4.

def array_front9(nums):
  if len(nums) > 3:
    for i in range(4):
      if nums[i] == 9:
        return True
  else: 
    for j in range(len(nums)):
      if nums[j] == 9:
        return True
      
  return False


# Given an array of ints, return True if the sequence of numbers
# 1, 2, 3 appears in the array somewhere.

def array123(nums):
  for i in range(len(nums)):
    if i + 2 < len(nums):
      if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] ==3:
        return True
  return False

# Given a string name, e.g. "Bob", return a greeting of the 
# form "Hello Bob!".

def hello_name(name):
  return 'Hello ' + name + '!'


# Given two strings, a and b, return the result of putting them 
# together in the order abba, e.g. "Hi" and "Bye" returns 
# "HiByeByeHi".

def make_abba(a, b):
  return a +b + b + a


# The web is built with HTML strings like "<i>Yay</i>" which 
# draws Yay as italic text. In this example, the "i" tag makes
# <i> and </i> which surround the word "Yay". Given tag and word 
# strings, create the HTML string with tags around the word, e.g. 
# "<i>Yay</i>".

def make_tags(tag, word):
  return '<'+ tag + '>' + word + '</' + tag + '>'


# Given an "out" string length 4, such as "<<>>", and a word, 
# return a new string where the word is in the middle of the 
# out string, e.g. "<<word>>".

def make_out_word(out, word):
  return out[:2] + word + out[2:]

# Given a string, return a new string made of 3 copies of the 
# last 2 chars of the original string. The string length will 
# be at least 2.

def extra_end(str):
  return str[len(str)-2: len(str)] * 3
 

# def first_two(str):
#   first_chars = str[:2]
#   return first_chars * 3

# print(first_two('Hello'))

#Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
def first_half(str):
  the_size = len(str) /2
  
  return str[:the_size]

def without_end(str):
  the_string = str[1:]
  the_string = the_string[:len(the_string)]
  return the_string

print(without_end('Hello'))

# Given a string, return a version without the first and last char, so "Hello" 
# yields "ell". The string length will be at least 2.

def without_end(str):
  the_string = str[1:]
  the_string = the_string[:len(the_string) -1]
  return the_string

# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter 
# string on the outside and the longer string on the inside. The strings will not be the same 
# length, but they may be empty (length 0).

def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  else:
    return a + b+ a
  
  # Given 2 strings, return their concatenation, except omit the first char of each. 
  # The strings will be at least length 1.

def non_start(a, b):
  return a[1:] + b[1:]

# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. 
# The string length will be at least 2.

def left2(str):
  two_characters = str[:2]
  return str[2:] + two_characters