def task():
    print("Step 1")
    print("Step 2")
    print("Step 3")
    return 100
    print("Step 4")
    print("Step 5")

def task2(x,y):
    print(x+y)

# task2("Livin","kumar")
# a=task()+100
# print(a)


# def sum(a,b,c,d):
#     return a+b+c+d 

# print(sum(23,32,45,20)-20)


b=100

def scope():
    a=10
    print(f"From Inside The Number Is: {b}")

def scope2():
    print(b)
   
scope() 
scope2()
