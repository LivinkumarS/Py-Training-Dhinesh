# try: 
#     print(1/0)
# except ZeroDivisionError:
#     print("A number cannot be divisible by Zero!")
# except TypeError:
#     print("A number cannot be divisible by a string!")

# print("Step1")
# print("Step2")
# print("Step3")

while 1:
    try:
        number = int(input("Enter The Number: "))
        if number%2==0:
            print("Even Number")
        else:
            print("Odd Number")
    except ValueError:
        print("Please Enter valid Number!")
