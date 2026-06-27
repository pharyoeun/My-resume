# exercise 1
numbers = [3, 7, 12, 18, 25]

target = int(input("Enter a number: "))

for num in numbers:
    if num == target:
        print("Number found")
        break
else:
    print("Number not found")

# ex2
numbers = [1, 3, 5, 8, 9]

for num in numbers:
    if num % 2 == 0:
        print("First even number:", num)
        break
else:
    print("No even numbers found")

# ex3
guesses = [4, 8, 12, 15, 20]
secret = 15

for guess in guesses:
    if guess == secret:
        print("Correct guess")
        break
else:
    print("Secret number not guessed")

# ex4
numbers = [5, 8, 12, 7]

for num in numbers:
    if num < 0:
        print("Negative number found")
        break
else:
    print("All numbers are positive")
# ex5
word = input("Enter a word: ")

seen = set()

for char in word:
    if char in seen:
        print("Duplicate character found:", char)
        break
    seen.add(char)
else:
    print("All characters are unique")
# ex6
number = int(input("Enter a positive integer: "))

if number < 2:
    print("Not prime")
else:
    for i in range(2, number):
        if number % i == 0:
            print("Not prime")
            break
    else:
        print("Prime number")
    #ex7
    list1 = [1, 4, 7, 9]
    list2 = [2, 5, 7, 10]

    for num in list1:
        if num in list2:
            print("Common number:", num)
            break
    else:
        print("No common numbers")
# ex8
password = input("Enter a password: ")


for char in password:
    if not char.isalnum():
        print("Invalid password")
        break
else:
    print("Password accepted")
#ex9
numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]

for i in range(1, 11):
    if i not in numbers:
        print("Missing number:", i)
        break
else:
    print("No missing number")
# ex10
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

for i in range(len(numbers) - 1):
    if numbers[i + 1] != numbers[i] + 1:
        print("Not consecutive")
        break
else:
    print("Sequence is consecutive")