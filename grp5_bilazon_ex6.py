#Write a Python function to find the maximum of three numbers.

def max_of_three(a, b, c):
    return max(a, max(b, c))

print(max_of_three(2003, 11, 26))



#Write a Python function to sum all the numbers in a list.

def sum_list(numbers):
    return sum(numbers)

print(sum_list([11, 26, 2, 20, 14]))



#Write a Python program to reverse a string.

def reverse_string(s):
    return s[::-1]

print(reverse_string("Hello")) 



#Write a Python function that accepts a string and counts the number of upper and lower case letters.

def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

upper, lower = count_case("Hello World")
print("Uppercase:", upper)  
print("Lowercase:", lower)  



#Write a Python function that takes a list and returns a new list with distinct elements from the first list.

def distinct_elements(lst):
    return list(set(lst))

print(distinct_elements([1, 2, 2, 3, 4, 4, 5]))
