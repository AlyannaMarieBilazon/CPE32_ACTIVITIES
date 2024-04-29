#Python program find difference between each number in the array and the average of all numbers
def find_difference(arr):
    avg = sum(arr) / len(arr)
    differences = [num - avg for num in arr]
    return differences

arr = [1, 2, 3, 4, 5]

print(find_difference(arr))

#Python program to convert a string in an array
def string_to_array(s):
    return list(s)

s = "Alyanna Marie"

print(string_to_array(s))

#Python program to split an array in two and store even numbers in one array and odd numbers in the other.
def split_even_odd(arr):
    even_nums = [num for num in arr if num % 2 == 0]
    odd_nums = [num for num in arr if num % 2 != 0]
    return even_nums, odd_nums

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even, odd = split_even_odd(arr)
print("Even numbers:", even)
print("Odd numbers:", odd)

#Python program to perform insertion sort on an array.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [12, 11, 13, 5, 6]

print("Original array:", arr)
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
