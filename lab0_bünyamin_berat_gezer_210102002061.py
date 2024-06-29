my_name = "BÜNYAMİN BERAT GEZER "
my_id = "210102002061"
my_email = "b.gezer2021@gtu.edu.tr"

def problem1():
    your_name=input("please enter your name : ")

    return f"Hi all, This is {your_name}"

print("running problem 1")
print(problem1())

def problem2():
    a = input("please enter some input: ")
    return f"input was {a}"

print("running problem 2")
print(problem2())

def problem3():
    number1=int(input("please enter first number : "))
    number2=int(input("please enter second number: "))
    total=number1+number2
    return total

print("running problem 3")   
print(problem3())

def problem4():
    x=float(input("please enter a first float number "))
    Y=float(input("please enter a second float number "))
    sum=x+Y
    return sum

print("running problem 4")
print(problem4())

def problem5():
    R=int(input("please enter a integer first number : " ))
    T=int(input("please enter a integer second number : " ))
    modula=R%T
    return modula 

print("running problem 5")
print(problem5())

def problem6():
    r=float(input("please enter a radius : "))
    h=float(input("please enter a height : "))
    pi=3.141592
    Volume_of_the_cylinder = r*r*h*pi   
    return Volume_of_the_cylinder
print("running problem 6")
print(problem6())

def problem7():
    d=float(input("please enter one side(d) : "))
    perimeter_of_asquare=4*d
    return f"the perimeter of the square is {perimeter_of_asquare}."
print("running problem 7")    
print(problem7())

if __name__ == "__main__":
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")
