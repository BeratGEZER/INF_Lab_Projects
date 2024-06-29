my_name = "Bunyamin Berat Gezer "
my_id = "210102002061"
my_email = "b.gezer2021@gtu.edu.tr"


def problem1():
    f=float(input("Enter Fahrenheit degree:"))
    c=(f-32)*(5/9)
    return c


def problem2():
    c=float(input("Enter Celsius degree:"))
    f=c*(9/5)+32
    return f


def problem3() : 
    n=int(input("Enter a number:"))
    return 2*n**2-n



def problem4():

    n=int(input("Enter a number:"))
    l0=2
    l1=1
    sum=l0+l1
    i=1
    if n==0 :
        return 2
    if n==1 : 
        return 1
    if n==2 :
        return sum   
    if n >2 :
        while i<n :
            a=l1
            l1=l0+l1
            l0=a
            i=i+1
    return l1
        
        

            
def problem5():
    input1=str(input("Enter a string:"))
    return input1[::-1]


def problem6():   
    a=str(input("Enter a string:"))
    unwanted="!#$%&\"'()*+,-./:;<=>?@[\\]^_`{|}~"          
    Str_1=""
    for i in a :
        if i in unwanted : 
            continue
        else : 
            Str_1=Str_1+i
    return Str_1
    


def problem7():
    input1=int(input("Enter input:"))
    str_berat=""

    if input1==0 :
        return 0    
    if input1==1 :
        return 1    
    if input1==2 :
        return 2    
    if input1==3 :
        return 3    
    if input1>0:
        while input1 >= 3  :
            a=input1%4
            str_berat=str_berat+str(a)
            input1=input1//4            
            if 0<input1<3:
                str_berat+=str(input1)
                
        return   str_berat[::-1]
    elif input1 < 0 :
        input1=abs(input1)
        while input1 >= 3  :
            a=input1%4
            str_berat=str_berat+str(a)
            input1=input1//4     
            if 0<input1<3:
                str_berat+=str(input1)       
        return   "-"+str_berat[::-1]




def problem8():
    input1=input("Enter input:") 
    opening = ["(","[","{"]
    closing = ["]",")","]","}"]
    pair = { ')' : '(' ,  ']' :'[' , '}' :'{'  }
    liste=[] 


    if len(input1)%2==0 :
        for i in input1:
            if i in opening :
                liste.append(i)
            if i in closing :
                if not liste: 
                    return False
                elif liste.pop() != pair[i]  :
                    return False
                else : 
                    continue
        
        if not liste: 
            return True
        else: 
            return False
    elif len(input1)%2==1:
        return False
    return True



def problem9():
    input1=str(input("Enter a string:"))
    liste1=input1.split(" ")
    return len(liste1[-1])





def problem10():
    route=input("Enter the exit route:")
    e=0
    w=0
    n=0
    s=0
    for i in route :
        if i == "e" :
            e+=1
        if i == "w" :
            w+=1
        if i == "n" :
            n+=1
        if i == "s" :
            s+=1    
    number1=e-w
    number2=n-s
    lenght_of_route=(number1**2)+(number2**2)
    root=lenght_of_route/2
    x0=0
    x1=100
    while x0<x1:
        x2=0.5*(root+lenght_of_route/root)
        root=x2
        x0=x0+1
    return x2
print(problem10())
    
 


# if __name__ == "__main__":
#     print(f"My name is {my_name}.")
#     print(f"My number is {my_id}.")
#     print(f"My email is {my_email}.")



#     print("Running problem 1")
#     print( problem1() )
    
#     print("Running problem 2")
#     print( problem2() )

#     print("Running problem 3")
#     print( problem3() )

#     print("Running problem 4")
#     print( problem4() )
    
#     print("Running problem 5")
#     print( problem5() )
    
#     print("Running problem 6")
#     print( problem6() )

#     print("Running problem 7")    
#     print( problem7() )
    
#     print("Running problem 8")
#     print( problem8() )
    
#     print("Running problem 9")
#     print( problem9() )
    
    # print("Running problem 10")
    # print( problem10() )





            








    
            

            
