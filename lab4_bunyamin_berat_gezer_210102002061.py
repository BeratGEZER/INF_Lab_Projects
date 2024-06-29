my_name = "Bunyamin Berat Gezer"
my_id = "210102002061"
my_email = "b.gezer2021@gtu.edu.tr"

def problem1(list,index):
    if index>len(list)-1 or index<0 :
        return None
    
    return list[index]



def problem2(list,index):
    if index>len(list)-1 or index<0 or len(list)==0 :
        return list
    else:
        list.pop(index)
        return list



def problem3(list,t_f):
    if t_f==True :
        list.sort()
        return list
    if t_f== False : 
        list.sort()
        return list[::-1]



def problem4(list_of_numbers,list_of_weightes):
    avarage_upper=0
    avarage_lower=0
    for i in range(len(list_of_weightes)):
        avarage_upper+=list_of_weightes[i]*list_of_numbers[i]
        avarage_lower+=list_of_weightes[i]
        avarage=avarage_upper/avarage_lower
    return float(avarage)        
    
# print(problem4([1, 2, 3], [.5, .5, 5]))



def problem5(list1,list2):

    min1=min(list1,list2)
    max2=max(list1,list2)
    r=0
    sum_list=[]
    for i in min1:
        for a in max2 :
            if i==a and i not in sum_list :
                sum_list.append(i)
                r+=1
    return r
# print(problem5([1,2,3,4], [3,2,1,5]))


def problem6(list1):
    if len(list1)==1:
        if len(list1)!=len(list1[0]):
            return None
        
    for i in range(1,len(list1)):
        if len(list1[i])!=len(list1[i-1]) or len(list1)!=len(list1[i-1]):
            return None
    if len(list1)==1:
        return float(list1[0][0])

    if len(list1)==2 :
        n1=list1[0][0]*list1[1][1]
        n2=list1[0][1]*list1[1][0]
        return float(n1-n2)
    if len(list1)==3:
        newlist=[]
        for x in list1:
            newlist.append(x)

        newlist.append(list1[0])
        newlist.append(list1[1])

        n1=newlist[0][0]*newlist[1][1]*newlist[2][2]
        n2=newlist[1][0]*newlist[2][1]*newlist[3][2]
        n3=newlist[2][0]*newlist[3][1]*newlist[4][2]
        sum1=n1+n2+n3

        n4=newlist[0][2]*newlist[1][1]*newlist[2][0]
        n5=newlist[1][2]*newlist[2][1]*newlist[3][0]
        n6=newlist[2][2]*newlist[3][1]*newlist[4][0]
        sum2=n4+n5+n6
        
        return float(sum1-sum2)

    if len(list1)==4:
        z1=list1[0][0]*list1[1][1]*list1[2][2]*list1[3][3]
        z2=list1[0][0]*list1[1][3]*list1[2][1]*list1[3][2]
        z3=list1[0][0]*list1[1][2]*list1[2][3]*list1[3][1]
        z4=list1[0][1]*list1[1][3]*list1[2][2]*list1[3][0]
        z5=list1[0][1]*list1[1][0]*list1[2][3]*list1[3][2]
        z6=list1[0][1]*list1[1][2]*list1[2][0]*list1[3][3]
        z7=list1[0][2]*list1[1][0]*list1[2][1]*list1[3][3]
        z8=list1[0][2]*list1[1][3]*list1[2][0]*list1[3][1]
        z9=list1[0][2]*list1[1][1]*list1[2][3]*list1[3][0]
        z10=list1[0][3]*list1[1][2]*list1[2][1]*list1[3][0]
        z11=list1[0][3]*list1[1][0]*list1[2][2]*list1[3][1]
        z12=list1[0][3]*list1[1][1]*list1[2][0]*list1[3][2]
        z13=list1[0][0]*list1[1][3]*list1[2][2]*list1[3][1]
        z14=list1[0][0]*list1[1][1]*list1[2][3]*list1[3][2]
        z15=list1[0][0]*list1[1][2]*list1[2][1]*list1[3][3]
        z16=list1[0][1]*list1[1][0]*list1[2][2]*list1[3][3]
        z17=list1[0][1]*list1[1][3]*list1[2][0]*list1[3][2]
        z18=list1[0][1]*list1[1][2]*list1[2][3]*list1[3][0]
        z19=list1[0][2]*list1[1][3]*list1[2][1]*list1[3][0]
        z20=list1[0][2]*list1[1][0]*list1[2][3]*list1[3][1]
        z21=list1[0][2]*list1[1][1]*list1[2][0]*list1[3][3]
        z22=list1[0][3]*list1[1][0]*list1[2][1]*list1[3][2]
        z23=list1[0][3]*list1[1][2]*list1[2][0]*list1[3][1]
        z24=list1[0][3]*list1[1][1]*list1[2][2]*list1[3][0]
    return float((z1+z2+z3+z4+z5+z6+z7+z8+z9+z10+z11+z12)-(z13+z14+z15+z16+z17+z18+z19+z20+z21+z22+z23+z24))

   
       
def problem7(accounts,source,lira,kurus):
    if source<0 or len(accounts)<=source :
        return accounts

    if float(accounts[source])-(lira+(kurus/100))<0:
        return accounts

    if float(accounts[source])-(lira+(kurus/100))>=0 : 
        new_account_index=float(accounts[source])-(lira+(kurus/100))
        new_account_index=round(new_account_index,3)

        new_account_index=f"{new_account_index:.2f}"
        if new_account_index=="0.00":
            new_account_index="0"

        accounts.pop(source)
        accounts.insert(source,str(new_account_index))

        return accounts




def problem8(accounts,source,destination,lira,kurus,fee=False):
    coin=lira+(kurus/100)
    
    
    if source==destination:
        return accounts
    if source<0 or destination<0 or source>=len(accounts) or destination>=len(accounts):
        return accounts
    if float(accounts[source])-(coin)<0:
        return accounts

    if float(accounts[source])-(lira+kurus/100)>=0:
        if fee==True and float(accounts[source])-(coin)==0:
            return accounts
        if fee==True:
            if (coin)>=10:
                fee1=(coin)*1/100
                fee1=f"{fee1:.2f}"
                if  float(accounts[source])-(coin)+(float(fee1))>=0:
                    new_account_source=float(accounts[source])-((coin)+float(fee1))
                    k=0
                    for f in str(new_account_source):
                        if f==".":
                            k+=1
                            if k == 2 and f==0:
                                new_account_source=new_account_source
                            if k>2:
                                new_account_source=f"{new_account_source:.2f}"
                                

                                
                                
                    accounts.pop(source)
                    accounts.insert(source,new_account_source)
                    transfer_coin=(lira+kurus/100)
                    transfer_coin=f"{transfer_coin:.4}"
                    new_destination=float(transfer_coin)+float(accounts[destination])
                    new_destination=f"{new_destination:.4}"
                    accounts.pop(destination)
                    accounts.insert(destination,new_destination)
                    return accounts
                else:
                    return accounts
            else:
                fee2=0.10
                
                if  float(accounts[source])-((coin)+fee2)>=0:
                    r=0
                    new_account_source=float(accounts[source])-((coin)+fee2)
                    round(new_account_source,3)
                    for a in str(new_account_source):
                        if a==".":
                            r+=1
                            if r == 2 and a==0:
                                new_account_source=new_account_source
                            if r>2:
                                new_account_source=f"{new_account_source:.2f}"
                    accounts.pop(source)
                    accounts.insert(source,str(new_account_source))
                    transfer_coin=(lira+kurus/100)
                    transfer_coin=f"{transfer_coin:.2f}"
                    new_destination=float(transfer_coin)+float(accounts[destination])
                    new_destination=f"{new_destination:.4}"
                    accounts.pop(destination)
                    accounts.insert(destination,str(new_destination)) 
                    return accounts
                else:
                    return accounts
    if float(accounts[source])-(coin)>=0:
        if fee==False :
            if float(accounts[source])-(coin)>=0:
                new_account_source=float(accounts[source])-coin
                
                z=0
                new_account_source=f"{new_account_source:.2}"
                for i in new_account_source:
                    if i ==".":
                       z+=1
                       if z>=2:
                            new_account_source=f"{new_account_source:.2}" 
                            break  
                    else:
                        new_account_source+="0" 
                        break       
                if new_account_source=="0.00":
                    new_account_source=="0"
                accounts.pop(source)
                accounts.insert(source,str(new_account_source))
                new_destination=coin+float(accounts[destination])
                new_destination=round(new_destination,3)
                new_destination=f"{new_destination:.4}"
                accounts.pop(destination)
                accounts.insert(destination,str(new_destination))
                return accounts
            else:
                return accounts
        


def problem9(number_of_students):
    list_of_students=[]
    bom_list=[]
    t_f=True
    bom_9=0
    x=0

    for i in range(number_of_students):
        bom_list.append(1)
    for x in range(1,number_of_students+1):
        list_of_students.append(x)
    while t_f==True:
        for i in range(len(list_of_students)):
            bom_9+=bom_list[i]
            x+=1
            if bom_9==9:
                bom_list[(x-1)%len(list_of_students)]=0
                bom_9=0
            if bom_list.count(1)==1 :
                bomm=bom_list.index(1)
                return list_of_students[bomm]


        
def problem10(list1):
    str=""

    if len(list1)==1 or len(list1)==0:
        return None

    for i in list1:                   
        if list1.count(i)>1 and i not in str:
           str+=i 
    
   

    if str=="":
        return None
    
    return str        
        
