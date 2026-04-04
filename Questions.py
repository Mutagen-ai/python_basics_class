#1 Even or odd checker
import random
number = int(input("Enter number:"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#Simple calculator
num1= float(input("Enter first number:"))
operator = input("Enter operator (+, -, *, /):")
num2 = float(input("Enter second number"))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print(num1 / num2)
else:
    print("Invalid operator")
    
#Positive, negative or zero
number = float(input("Enter number:"))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")
    
    
#Number guessing game


secret_number = random.randint(1, 10)
print("Welcome to the guess the number game!")
print("I'm thinking of a number between 1 and 10. Can you guess what it is?")

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulations! You guessed the number correctly")
        break
    elif guess > secret_number:
        print("Your guess is too high. Guess again.")
    else:
        print("Your guess is too low. Guess again.")
        
        
#Print numbers 1-5
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i)
    
    
# 6
n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum:", total)


# 7
text = input("Enter a string: ")

vowels = "aeiou"
count = 0

for letter in text.lower():
    if letter in vowels:
        count = count + 1

print("Number of vowels:", count)


#8
correct_password = "python123"

while True:
    password = input("Enter the password: ")

    if password == correct_password:
        print("Access granted!")
        break
    else:
        print("Wrong password. Try again.")
        

#9
numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total = total + number

average = total / len(numbers)

print("Sum:", total)
print("Average:", average)

#10
fruits = ["apple", "banana", "cherry", "mango", "orange"]

for fruit in fruits:
    print(fruit)
    
#11
prices = []

for i in range(5):
    price = float(input(f"Enter price of item {i + 1}: "))
    prices.append(price)

total = 0

for price in prices:
    total = total + price

print("Total cost:", total)

#12
for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        
#13
text = input("Enter a string: ")

reversed_text = ""

for letter in text:
    reversed_text = letter + reversed_text

print("Reversed:", reversed_text)


#14
marks = float(input("Enter student marks: "))

if marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")
    
#33 Loop through a list and print numbers and its square
numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
    print("Number:", number, "Square:", number * number)

#34 Filter Even Numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

#35 Sum of list using loop
numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
    total = total + number
print("Total sum:", total)

#36 Loop through dictionary
students = {
    "Elizabeth": 85,
    "Tony": 92,
    "Carol": 78,
    "David": 65
    }
for name, score in students.items():
    print("Name", name, "Score", score)

#37 Find the highest value in dictionary
prices = {
    "laptop": 1200,
    "phone": 800,
    "tablet": 950,
    "headphones": 300
}
highest_item = ""
highest_price = 0
for item, price in prices.items():
    if price > highest_price:
        highest_price = price
        highest_item = item
print("The most expensive item:", highest_item)
print("Price:", highest_price)

#38 Count frequency of items in a list
numbers = [1, 2, 2, 3, 1, 2]
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] = frequency[number] + 1
    else:
        frequency[number] = 1
print(frequency)

#Loop through a set and for each number print number and its double
numbers = {1, 2, 3, 4, 5, 6, 7, 8}
for number in numbers:
    print("Number:", number, "Double:", number * 2)