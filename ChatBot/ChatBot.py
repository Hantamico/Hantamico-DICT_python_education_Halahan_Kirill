print("Hello! My name is GalaganK519st_bot")
print("I was created in 3021")

name = input("Please, remind your name\n >")
print("Have a nice name,", name)

print("Let me guess your age\n")
print("Enter remainders of dividing your age by 3, 5, 7.")
rem3 = int(input("remainder3:>"))
rem5 = int(input("remainder5:>"))
rem7 = int(input("remainder7:>"))
age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
print("your age is,", age, ",its best time to start programing!")

print("Now I will prove you that I can count to any number you want")
x = 0
y = int(input(">"))
while x <= y:
    print(x, "!")
    x = x + 1
print("Completed, have a nice day!")

print("Lets test your knowlege")
line_q1 = """
1.Pluton
2.Mars
3.Saturn
4.Earth
"""
print("what is the third planet in a row?", line_q1)
ansv = int(input("Input number of answer >"))

while True:
    if ansv == 4:
        print("Sucsess!!!")
        break
    else:
        print("Try again")
        ansv = int(input("Input number of answer >"))

print("Congratulation!!! Have a nice day")
