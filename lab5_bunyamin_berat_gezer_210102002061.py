my_name = "Bunyamin Berat Gezer"
my_id = "210102002061"
my_email = "b.gezer2021@gtu.edu.tr"



def problem1(list_of_integer,repeat):
    value_of_retrun=[]
    kume=set(list_of_integer)
    kume=list(kume)

    if repeat<=0:
        return []
    for i in range(len(kume)):
        if repeat==list_of_integer.count(kume[i]):
            value_of_retrun.append(kume[i])
        else:
            continue
    return value_of_retrun

def problem2(dict1):

    values_of_dict=[]
    values=dict1.values()

    for i in values:
        values_of_dict.append(i)
    
    lenght=len(values_of_dict)
    values_of_dict.sort()

    if len(dict1)%2==1:

        return int(values_of_dict[int(((lenght/2)+0.5)-1)])

    else:
        toplam = (values_of_dict[int((lenght/2)-1)]+values_of_dict[int(((lenght/2)+1)-1)])
        if toplam % 2 == 0:
            return int((values_of_dict[int((lenght/2)-1)]+values_of_dict[int(((lenght/2)+1)-1)]) / 2)
        return ((values_of_dict[int((lenght/2)-1)]+values_of_dict[int(((lenght/2)+1)-1)])/2)


def problem3(filename):
    try:
        filename=open(filename,"r")
        words1=filename.readlines()
        new_list_total=[]
        list_of_dict=[]
        n_a="NA"
        
    
        keys=['name','credit','term','grade'] 
        values=[]  

        
            
        for i in words1:
            for x in i :
                if x=="\n":
                    i=i.replace("\n","")
                    new_list_total.append(i)
        for k in new_list_total:
            control=k
        
            k=k.split(', ')
            if len(k)==3:
                str=""
                for i in k[-1]:
                    if i==",":
                        continue
                    else:
                        str+=i
                    k.pop(-1)
                    k.append(str)
                    k.append(n_a)




            int_number1=k.pop(1)
            k.insert(1,int(int_number1))
            int_number2=k.pop(2)
            k.insert(2,int(int_number2))
            values.append(k)
        for l in values:
            dict1=dict(zip(keys,l))
            list_of_dict.append(dict1)





        return list_of_dict
    except:
        return []

def problem4(list_of_dict,term):

    if len(list_of_dict)==0 :
        return 0

    control=0
    for x in range(len(list_of_dict)):
        if list_of_dict[x]["term"]!=term:
            control+=1
    if control==len(list_of_dict):
        return 0
    

    dict_of_nots={"AA":4.0,"BA":3.5,"BB":3.0,"CB":2.5,"CC":2.0,"DC":1.5,"DD":1.0,"FF":0.0}

    sum_upper=0
    sum_lower=0
    for i in range(len(list_of_dict)):
        if list_of_dict[i]["grade"]=="NA" or list_of_dict[i]["term"]!=term:
            continue
        upper_of_equation=list_of_dict[i]["credit"]*dict_of_nots[list_of_dict[i]["grade"]]
        sum_upper+=upper_of_equation
        lower_of_equation=list_of_dict[i]["credit"]
        sum_lower+=lower_of_equation

    return float(sum_upper/sum_lower)

def problem5(anyfunc,n):

    if type(anyfunc(n)) != int:
        return False
    a=0
    strx=""
    for i in range(n+1):
        strx+=str(i)
    for x in strx:
        if x=="1":
            a+=1
    
    if anyfunc(n)==a:
        return True
    
    return False

def problem6(strx):

    list_of_combination=[]

    list_of_all_return=[]

    list_of_all=[[],[],[],[],[],[],[],[],[],[]]

    for i in strx:
        list_of_combination.append(i)

    tuple_of_combination=set(list_of_combination)

    

    for i in tuple_of_combination:
        list_of_all[0].append(i)
    
    tuple_of_combination=list(set(list_of_combination))

    for t in range(len(strx)-1):
        for i in strx:
            for x in list_of_all[t]:
                r=x+i
                if r not in list_of_all[t+1] :

                    list_of_all[t+1].append(r)
                else:
                    continue


    for i in range(len(list_of_all)):
        for i in list_of_all[i]:            
            list_of_all_return.append(i)

    list_of_all_returnx=list_of_all_return [:]

    for i in tuple_of_combination:
        for x in list_of_all_return:
            if list_of_combination.count(i)>=x.count(i) or x not in list_of_all_returnx:
                continue
            else:
                 list_of_all_returnx.remove(x)


   
    list_of_all_returnx.sort()
            
    return list_of_all_returnx

def problem7(strx,filename):
    strx.lower()
    filename=open(filename,"r")
    word1=filename.readlines()
    list_of_words=[]
    list_of_anagrams=[]

    for i in word1:
        if "\n" in i:
            new_list_of_word=i.replace("\n","")
            list_of_words.append(new_list_of_word)
        else:
            list_of_words.append(i)

    list_of_combination=[]

    list_of_all_return=[]

    list_of_all=[[],[],[],[],[],[],[],[],[],[]]

    for i in strx:
        list_of_combination.append(i)

    tuple_of_combination=set(list_of_combination)

    

    for i in tuple_of_combination:
        list_of_all[0].append(i)
    
    tuple_of_combination=list(set(list_of_combination))

    for t in range(len(strx)-1):
        for i in strx:
            for x in list_of_all[t]:
                r=x+i
                if r not in list_of_all[t+1] :

                    list_of_all[t+1].append(r)
                else:
                    continue


    for i in range(len(list_of_all)):
        for i in list_of_all[i]:            
            list_of_all_return.append(i)

    list_of_all_returnx=list_of_all_return [:]

    for i in tuple_of_combination:
        for x in list_of_all_return:
            if list_of_combination.count(i)>=x.count(i) or x not in list_of_all_returnx:
                continue
            else:
                 list_of_all_returnx.remove(x)


   
    list_of_all_returnx.sort()


    for i in list_of_all_returnx:
        if i in list_of_words:
            list_of_anagrams.append(i)


    return list_of_anagrams

def problem8(mm,sm):
    list_of_mm=[]
    list_of_sm=[]
    for i in mm:
        list_of_mm.append(i)

    for x in sm:
        list_of_sm.append(i)


    if len(list_of_mm) < len(list_of_sm) or len(list_of_mm[0]) < len(list_of_sm[0]):
        return False
    
    if len(list_of_sm) <= 0 or len(list_of_sm[0]) <= 0:
        return False

    for b in range(len(list_of_mm) - len(list_of_sm) + 1):
        for e in range(len(list_of_mm[0]) - len(list_of_sm[0]) + 1):
            if list_of_mm[b][e] == list_of_sm[0][0]:
                for r in range(len(list_of_sm)):
                    for a in range(len(list_of_sm[0])):
                        if list_of_mm[b+r][e+a] == list_of_sm[r][a]:
                            continue
                        else:
                            break
                    else:
                        continue
                    break
                else:
                    return True
    return False

def problem9(unzipped_str):
    str = ""
    bos_liste = []
    list_of_number=[]
    for i in range(10):
        bos_liste.append(i)

    for i in bos_liste:
        list_of_number.append("{}".format(i))
        
        
    for i in unzipped_str:
        if i not in str:
            str += "{}".format(i)
            if unzipped_str.count(i) != 1:
                str += "{}".format(unzipped_str.count(i))
    berat = 0
    for i in str:
        if i in list_of_number:
            berat = 1
            break
    if berat == 0:
        return (unzipped_str, 0)
        
    rate = int(round((((len(unzipped_str) - len(str))*100) / len(unzipped_str)),0))
    return (str, rate)
    
def problem10(list_of_number):
    list_of_number.sort()
    new_list_number=[]
    for i in list_of_number:
        new_list_number.append(i)

    for x in range(len(new_list_number)-1):
        if new_list_number[x+1]-new_list_number[x]==1:
            continue
        else:
            new_list_number.insert(x+1,int((new_list_number[x+1]+new_list_number[x])/2))

    if len(new_list_number)==len(list_of_number):
        new_list_number.append(new_list_number[-1]+1)

    
    for i in list_of_number:
        new_list_number.remove(i)

    

    return new_list_number[0]



