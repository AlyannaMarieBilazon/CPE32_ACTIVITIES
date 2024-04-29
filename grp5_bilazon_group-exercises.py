#1.Display numbers from -10 to -1 using for loop
for i in range(-10, 0):
    print(i)

#2. Use else block to display a message “Done” after successful execution of for loop
for i in range(-10, 0):
    print(i)
else:
    print("Done")

#3.Write a program to display all prime numbers within a range
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)

#4.Use a loop to display elements from a given list present at odd index positions
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in range(1, len(my_list), 2):
    print(my_list[index])

#5. Display numbers from a list using loop
#a. The number must be divisible by five
#b. If the number is greater than 150, then skip it and move to the next number
#c. If the number is greater than 500, then stop the l
#numbers = [12, 75, 150, 180, 145, 525, 50]
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    if num > 150:
        continue
    if num % 5 == 0:
        print(num)
