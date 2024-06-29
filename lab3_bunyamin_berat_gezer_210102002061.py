
my_name = "Bunyamin Berat Gezer "
my_id = "210102002061"
my_email = "b.gezer2021@gtu.edu.tr"




def problem1(a):
    for i in a :
        if i=="K":
            return True
    else:
        return False
    



def problem2(a,b,c,d):
    return float(min(a,b,c,d))







def problem3(a,b):
    if type(a) == float and b>a : 
        return int(a+1)    
    if type(a)==int  : 
        return a                 
    if a>b and b>=1 :
        return int(a)
    if a>b and b>=0.5 :
        return round(a)
    if a>b and 0<=b<0.5 : 
        return int(a)
    if a>b and b<0 : 
        return int(a-1)

# print(problem3(2,3))
     

def problem4(radius,height,pi=3.1415):
    return pi*radius**2*height



def problem5(radius, height, pi=3.1415):
    if (type(radius)==float or type(radius)==int) and (type(height)==float or type(radius)==int) and (pi==int or pi==float):
        return pi*radius**2*height
    else: 
        return  -1 
print(problem5(2.1,3.2,3))
 


def problem6(a):
    str_=""
    for i in a : 
        if True : 
            r=a.count(i)
            if r==1: 
                str_=str_+str(i)
            else: 
                continue
    return str_



def problem7(a):
    liste=[]
    for i in a : 
        liste.append(i)
    for i in range(0,len(liste)-1):
        if liste[i]<=liste[i+1] :
            continue
        else:
            return False
    return True    



def problem8(a):
    for i in a :            
        if True : 
            count_number=a.count(i)
            if count_number == 1 :
                continue
            else :
                return False
    return True





def problem9(row,column):

    if row==1 and column==1:
        return 1
    if row>1 and column==1 : 
        return 3
    if row==column :
        return 2
    
    return problem9(row-1,column-1)+problem9(row-1,column)



def problem10(a,b):
    r=0
    min_=min(len(a),len(b))
    for i in range(0,min_):
        if a[i]==b[i] :
            r+=1
        else:
            continue
    return r

print(problem9(1, 1))
print(problem9(4, 1))
print(problem9(9, 1))
print(problem9(row=5, column=5))
print(problem9(8, 8))
print(problem9(8, 3))
print(problem9(12, 7))








            


        








    














































































































