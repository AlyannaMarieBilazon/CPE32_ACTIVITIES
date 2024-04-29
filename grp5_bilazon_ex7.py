#1.Write a Python program to create an array of 3 integers and display the array items. 
#Access individual elements through indexes.
import array

arr = array.array('i', [1, 3, 5])

for item in arr:
    print(item)

#2 Write a Python program to append a new item to the end of the array.
import array

arr = array.array('i', [1, 3, 5, 7, 9])

print("Original array:", arr)

# Append 11 at the end of the array
arr.append(11)

print("New array:", arr)

#3. Write a Python program to reverse the order of the items in the array.
import array

arr = array.array('i', [1, 3, 5, 3, 7, 1, 9, 3])

print("Original array:", arr)

# Reverse the order of the items
arr.reverse()

print("Reverse the order of the items:", arr)

#4.Write a Python program to find out if a given array of integers contains any duplicate elements. 
#Return true if any value appears at least twice in the array, and return false if every element is distinct.
def has_duplicates(arr):
    return len(set(arr)) != len(arr)

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 4, 5]
arr3 = [1, 2, 2, 3, 4, 5]

print(has_duplicates(arr1))
print(has_duplicates(arr2))
print(has_duplicates(arr3))

#5.Write a Python program to find the first duplicate element in a given array of integers. 
#Return -1 if there are no such elements.
def first_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1

arr1 = [1, 2, 3, 4, 5, 4]
arr2 = [1, 2, 3, 4, 5]
arr3 = [1, 2, 2, 3, 4, 5]

print(first_duplicate(arr1))
print(first_duplicate(arr2))
print(first_duplicate(arr3))
