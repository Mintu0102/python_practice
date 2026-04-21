# for loops
# fruits = ["apple" , "seb"]
# for i in fruits:
#     print(i)

# score = [100, 200, 300, 400]
# total = sum(score)
# print(total)

# score = [100, 200, 200 ]
#
# maximum = 0
#
# for i in score:
#     if i > maximum:
#         maximum = i
# print(maximum)
# total_Sum = 0
# for i in range(1, 102874386427632621):
#     total_Sum += i
# print(total_Sum)

# for i in range(1, 101):
#     if i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else: print(i)

# project passwrod generator
# easy level
# import random
# letters = ["A", "B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# numbers = ["1","2","3","4","5","6","7","8","9","10"]
# symbols = ["@","#","$","!","%"]
#
# nr_letter = int(input("how many letters you want\n"))
# nr_number = int(input("how many number you want\n"))
# nr_symbol = int(input("how many symbol you want\n"))
#
# password = ""
#
# for char in range(0, nr_letter):
#     password += random.choice(letters)
#
# for num in range(0, nr_number):
#     password += random.choice(numbers)
#
# for symbol in range(0, nr_symbol):
#     password += random.choice(symbols)
#
# random.shuffle(password)
#
# print(f"your pass word is {password}")

# hard level
import random
letters = ["A", "B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["1","2","3","4","5","6","7","8","9","10"]
symbols = ["@","#","$","!","%"]

nr_letter = int(input("how many letters you want\n"))
nr_number = int(input("how many number you want\n"))
nr_symbol = int(input("how many symbol you want\n"))

password = []

for char in range(0, nr_letter):
    password.append(random.choice(letters))

for num in range(0, nr_number):
    password.append(random.choice(numbers))

for symbol in range(0, nr_symbol):
    password.append(random.choice(symbols))

random.shuffle(password)

print(f"your pass word is {password}")
passkey = ""
for key in password:
    passkey += key
print(f"pass key is {passkey}")

