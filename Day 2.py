# Datatypes and its error
# string
# integer
# float
# boolean
# print(type("Bilal"))
# print(type(1233456))
# print(type(123.4556))
# print(type(True))
#
# # conversion of datatype and typecasting
# print("123" + "345")
#
# print(int("123") + int("345"))

# print("Number of letters in your name " + str(len(input("Enter your name"))))

# mathematical operations
# print(123 +345)
# print(7 - 3)
# print(3 * 2)
# print(5 / 3)
# print(5 // 3)

# print(22 / 7)
# print(2**4)
# PEMDAS RULE IS IMPORTANT
#
# bmi = 84 / 1.5 ** 2
# print(bmi)
# print(int(bmi))
# print(round(bmi))
# print(round(bmi, 2))
# ye sab round off krne ke kaam aate hai

# f string
# score = 100
# height = 6.12
# is_winning = True
# print(f"Your score is; {score} , Your height is {height} , you {is_winning}")

# tip calculator project
print("Welcome to the Tip Generator")
bill = float(input("What was the total bill$"))
tip = int(input("how much the tip is 10, 20 ,30 "))
total_bill = tip / 100 * bill + bill
each_person = int(input("how many people split the bill"))
final_value = total_bill / each_person
print(f"Each person will pay$ {final_value}")




