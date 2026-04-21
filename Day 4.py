# random module
import random

# a = random.randint(2, 10)
# print(a)

# b = random.random() * 10
# print(b)

# c = random.uniform(2, 10)
#
# print(round(c))
# a = round(random.random())
# if a == 0:
#     print("tere satte me head hai")
# else:
#     print("tail hai satte me")

# fruits = ["mango", "seb", "kela"]
# fruits.extend(["angoor", "santra "])
#
# print(fruits)
# fruits[2] = "kharbuza"
# print(fruits)

# project rock paper scissor

user_choice = input("what you want to choose? 0 for rock, 1 for paper, 2 for scissor,\n ")
computer_choice = random.randint(0,2)
print(f"computer chose {computer_choice}")
if user_choice == 0 and computer_choice == 1:
    print("jeet gya tu")
elif user_choice == 1 and computer_choice == 2:
    print("jeeta tu")
elif user_choice == 0 and computer_choice == 2:
    print("jeet tu")
elif user_choice == 2 and computer_choice == 0:
    print("jeet gya gandu")
elif user_choice == computer_choice:
    print("draw")
else: print ("haar gya tu")
