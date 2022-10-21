#Question 1: Writing username function

def hello_name(user_name):
    user_name = input('What is your username: ')
    print('hello_' + user_name + '!')

hello_name('user_name')

#question 2: printing odd numbers

def first_odds():
    x = range(101)
    for num in x:
        if num % 2 != 0:
            print(num) 
first_odds()

#question 3: max number in a list

def max_num_in_list(a_list):
    max = list[0]
    for x in list:
        if x > max:
         max = x
   
    return max
print(max_num_in_list([1, 2, -8, 0]))
#confused on why I can't get this to work but moving on now

#Problem 4: determining leap years

def is_leap(year):
    
    leap = False  
    if (year % 400 == 0) and (year % 100 == 0):      
        leap = True
    elif (year % 4 ==0) and (year % 100 != 0):
        leap = True
    else:      
        pass
    
    return leap

result = is_leap(1997)
print(result)

#Problem 5: checking for consecutive numbers

def is_consecutive(a_list):

    return sorted(a_list) == list(range(min(a_list), max(a_list)))
      
a_list = [2, 3, 1, 4, 5]
print(is_consecutive(a_list))