# if else statements
# ek = se value assign hoti nad == se equality check hoti
# print("WELCOME TO THE TICKET COUNTER")
#
# height = int(input("Teri lambai kitni hai\n"))
#
# if height >=80:
#     print("Jaa jhool")
# else:
#     print("nikal lode")

# print("This program will help you to determine odd or even")
# number = int(input("Enter your number"))
#
# if number % 2 == 0:
#     print("pura jayega")
# else: print ("bhakkkk")

# nested if else statement

# print("WELCOME TO THE TICKET COUNTER")
#
# height = int(input("Teri lambai kitni hai\n"))
# age = int(input("Umar bata behen ke lode\n"))
#
# if height >=80:
#     if age >=18:
#         print("your tickt is 15 $")
#     else: print("your ticket 5$")
# else:
#     print("nikal lode")

# BMI calculator by using if else statement
# print("Welcome the BMI Calculator")
# weight = int(input("Kitne kilo ka hai"))
# height = float(input("lambai bata"))
#
# bmi = weight // (height ** 2)
#
# print("Your bmi is", int(bmi))
#
# if bmi < 18.5:
#     print("Underwieght")
# elif bmi >= 18.5 and bmi <=25:
#     print("normal")
# else: print("mote behenchod")

# print("Welcometo the roller coster")
# height = int(input("kitna lamba hai?\n"))
# bill = 0
# if height >=100:
#     print("JAA sakte ho")
#     age = int(input("umar kitni hai\n"))
#     if age <=12:
#         bill = 5
#         print("tu 5$ de behen ke lund")


#
#     elif age >=13 and age <=18:
#         bill = 10
#         print("tu 10$ dega ")
#     elif age > 19:
#         bill = 50
#         print("50$ de randike")
#     else:
#         print("tu 200$ dede")
#     photo_khichani = input("photo lega gaandu? HAAN ya na bol \n")
#     if photo_khichani == "haan" or photo_khichani== "HAAN":
#         bill += 3
#     print(f"total bill is {bill}")
# else: print("maachuda sakte lekin awaz mt krna")


# print("Welcome to python pizza delivery")
# size = input("what size do you want? S , M, L ")
# peperoni = input("peperoni chaiye ? ")
# extra_cheese = input("cheese chahiye")
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#      bill += 25
# else: print("invalid input")
#
#
# if peperoni == "y":
#     if size == "S":
#      bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "y":
#     bill += 1
#
# print(f"total bill is {bill}")

print("Welcome to the game")
way = input("where doyou want to go, left or right")
if way == "left":
    b = input("swim or wait")
    if b == "wait":
        c = input("which door, red , blue , yellow")
        if c == "yellow":
            print("you won")
        else: print("haar gya bhadwe")
    else: print("maa chudi teri to ")
else: print("maa chuda randi ke")



