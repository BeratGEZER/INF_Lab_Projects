
my_name = "Bunyamin Berat Gezer"
my_id = "210102002061"
my_email = "b.gezer2021@gtu.edu.tr"


def problem1():
    
    return my_name[0]



def problem2():
    
    a=int(input("Enter a number:"))
    my_name[a%len(my_name)]
    return  my_name[a%len(my_name)]





def problem3():
    
    input1=int(input("Enter first number:"))
    input2=int(input("Enter second number:"))
    input1=input1%len(my_name)
    input2=input2%len(my_name)
    return my_name[min(input1,input2):max(input1+1,input2+1)]





def problem4():
    a=input("Enter input:")
    vowels = { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    variable_0 = 0
    for i in a :
        if i in vowels:
            variable_0=variable_0+1 
    return variable_0
           
  



def problem5():   
    my_id ="210102002061"
    r=0
    for i  in my_id:
        r=r+int(i)
    return r



def problem6():
    n=int(input("Enter input:"))
    a=1
    for sayı in range(1, n+1) :  
         factoriel=a=a*sayı
    return factoriel





def problem7():
    number1=int(input("Enter a number:"))
    if  number1>=0 and number1%3==0 and number1%7==0 :
        return True        
    else:        

        return False



def problem8():  
    number1=int(input("Enter a number:"))
    if number1>=0 and number1%7==0 and number1%3==0 :
        return 3
    elif number1>=0 and number1%7==0 :
        return 2
    elif number1>=0 and number1%3==0 :
        return 1
    else :
        return None
                



def problem9():
    number=int(input("Enter a number:"))
    if number==2 :
         return True
    for i in range(2,number) :
        if number%i == 0 : 
             return False            
    else :
            return True



   

def problem10() : 
    number1=float(input("Enter a number:"))
    x0=number1/2
    d=1
    a=0.000000000000000000000000000000001
    while d > a : 
        x1 =0.5*(x0+(number1/x0))
        d = x0- x1
        x0=x1
    return x0

print(problem10())



# if __name__ == "__main__":
#     print(f"My name is {my_name}.")
#     print(f"My number is {my_id}.")
#     print(f"My email is {my_email}.")



  
# print("Running problem 1")
# print( problem1() )
    
# print("Running problem 2")
# print( problem2() )

# print("Running problem 3")
# print( problem3() )

# print("Running problem 4")
# print( problem4() )
    
# print("Running problem 5")
# print( problem5() )
    
# print("Running problem 6")
# print( problem6() )

# print("Running problem 7")
# print( problem7() )
    
# print("Running problem 8")
# print( problem8() )
    
# print("Running problem 9")
# print( problem9() )
    
# print("Running problem 10")
# print( problem10() )

    
    
    
    
    
    
    
    
    
    
    
    
        


