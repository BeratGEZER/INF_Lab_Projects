my_name = "Bunyamin Berat Gezer"
my_id = "210102002061"
my_email = "b.gezer2021@gtu.edu.tr"



def problem0():
    class p0:
        def __init__(self,number):
            self.number = number
        
        def get_value(self):
            return self.number
        
        def set_value(self,number):
            self.number = number
    
    return p0


def problem1():
    class p1:
        def __init__(self,number):
            if type(number) == int:
                self.number = number
            else:
                self.number = 0

        def get_value(self):
            return self.number

        def set_value(self,number):
            if type(number) == int:
                self.number = number
            else:
                pass
    
    
    return p1



def problem2():
    class p1:
        def __init__(self,x,y):
            self.x = x
            self.y = y

        def get_area(self):
            return self.x * self.y
  
        def get_perimeter(self):
            return 2*(self.x) + 2*(self.y)
    return p1


def problem3():
    class Grades:
        sifir = 0
        def __init__(self):
            self.liste = [0.0]

        def add_grade(self,x):
            if self.sifir == 0:
                del self.liste[0]

            self.liste.append(float(x))
            self.sifir = 1

        def remove_grade(self,x):
            if float(x) in self.liste:
                for k in self.liste:
                    if k == float(x):
                        self.liste.remove(k)
            else:
                pass

        def get_min(self):
            if not self.liste:
                return 0.0
            return float(min(self.liste))
        
        def get_max(self):
            return max(self.liste)
            
        def get_mean(self):
            total = 0
            len_list = len(self.liste)
            for i in self.liste:
                total += i
            if len_list == 0 or total == 0:
                return 0.0
            return total / len_list

        def get_median(self):            
            if not self.liste:
                return 0.0
            self.liste.sort()
            if len(self.liste) % 2 == 0:
                return float((self.liste[len(self.liste) // 2] + self.liste[len(self.liste) // 2 - 1]) / 2)
            else:
                return float(self.liste[len(self.liste) // 2])
    return Grades






def problem4():
    class Movie:
        def __init__(self,movie_name,director,year,rating = 0.,length=0):
            self.movie_name = movie_name
            self.director = director
            self.year = year

            if type(rating) == float:
                if rating >= 0. :
                    if rating <= 10.0 :
                        self.rating = rating
                else:
                    self.rating = 0.0
            else:
                self.rating = 0.0
            if type(length) == int:
                if length >= 0 :
                    if  length <= 500:
                        self.length = length
                    else:
                        self.length = 0
                else:
                    self.length = 0
            else:
                self.length = 0

        def get_movie_name(self):
            return self.movie_name

        def get_director(self):
            return self.director

        def get_year(self):
            return self.year

        def get_rating(self):
            return self.rating

        def get_length(self):
            return self.length

        def set_rating(self,x):
            if type(x) == float:
                if x >= 0.0 :
                    if x <= 10.0:
                        self.rating = x

        def set_length(self,y):
            if type(y) == int:
                if y >= 0 :
                    if  y <= 500 :
                        self.length = y 

    return Movie





def problem5():
    pass




def problem6():
    class Node:
        def __init__(self,x,y,z):
            self.x = x
            self.y = y
            self.z = z



        def get_node(self):
            return (self.x,self.y,self.z)




        def get_distance(self):
            coordinate_value=(self.x**2 + self.y**2 + self.z**2)**0.5
            return coordinate_value



        def __add__(self,other):

            xi = self.x + other.x
            yj = self.y + other.y
            zk= self.z + other.z

            return Node(xi,yj,zk)

        def __str__(self):
            return f"<{self.x}, {self.y}, {self.z}>"


        def __gt__(self,other):
            coordinate1 = (self.x**2 + self.y**2 + self.z**2)**0.5
            coordinate2 = (other.x**2 + other.y**2 + other.z**2)**0.5
            return coordinate1 > coordinate2

        def __ge__(self, other):
            return self.get_distance() >= other.get_distance()


        def __lt__(self,other):
            coordinate1 = (self.x**2 + self.y**2 + self.z**2)**0.5
            coordinate2 = (other.x**2 + other.y**2 + other.z**2)**0.5
            return coordinate1 < coordinate2



        def __le__(self,other):
            coordinate1 = (self.x**2 + self.y**2 + self.z**2)**0.5
            coordinate2 = (other.x**2 + other.y**2 + other.z**2)**0.5
            return coordinate1 <= coordinate2



        def __eq__(self, other):
            if self.x != other.x or self.y != other.y or self.z != other.z:
                return False
            else:
                return True
            
    return Node



def problem7():
    
    from random import randint
    class NodeCloud:
        
        def __init__(self, n):
            self.list_tuple = []
            for i in range(int(n)):
                self.list_tuple.append((randint(-20, 20), randint(-20, 20), randint(-20, 20)))
        
        def get_nodes(self):
            return self.list_tuple
        
        def get_outermost(self):
            max_distance = 0
            outermost_node = None
            for x, y, z in self.list_tuple:
                distance = x**2 + y**2 + z**2
                if distance > max_distance:
                    max_distance = distance
                    outermost_node = (x, y, z)
            return outermost_node
        
        def add_node(self, x, y, z):
            if (x, y, z) not in self.list_tuple:
                self.list_tuple.append((x, y, z))
        
        def get_sum(self):
            Node=problem6()
            xsum = 0
            ysum = 0
            zsum = 0
            for x, y, z in self.list_tuple:
                xsum += x
                ysum += y
                zsum += z
            return Node(xsum, ysum, zsum)
    return NodeCloud






def problem8():
    class Encoder:
        def __init__(self,x):
            list = []
            for i in x:
                no =  ord(i)
                if (no >= 48 and no <= 57) or (no >= 65 and no <= 90) or (no >= 97 and no <= 122):
                    list.append(ord(i))
            self.list = list[:]
        

        def __str__(self):
            return ''.join(chr(i) for i in self.list)

            
        def morse(self):
            list3 = []
            for i in self.list:
                list3.append("{}".format(chr(i).upper()))
            list4 = []
            for i in list3:
                list4.append(ord(i))
            list2 = []
            for i in list4:
                if i == 48:  
                    list2.append("-----")
                    ##0
                elif i == 49:
                    list2.append(".----") 
                    ##1
                elif i == 50:
                    list2.append("..---")
                    ##2
                elif i == 51:
                    list2.append("...--")
                    ##3
                elif i == 52:
                    list2.append("....-")
                    ##4
                elif i == 53:
                    list2.append(".....")
                    ##5
                elif i == 54:
                    list2.append("-....")
                    ##6
                elif i == 55:
                    list2.append("--...")
                    ##7
                elif i == 56:
                    list2.append("---..")
                    ##8
                elif i == 57:
                    list2.append("----.") 
                    ## 9
                elif i == 65:
                    list2.append(".-") 
                    #A
                elif i == 66:
                    list2.append("-...") 
                    #B
                elif i == 67:
                    list2.append("-.-.") 
                    #C
                elif i == 68:
                    list2.append("-..") 
                    #D
                elif i == 69:
                    list2.append(".") 
                    #E
                elif i == 70:
                    list2.append("..-.") 
                    #F
                elif i == 71:
                    list2.append("--.") 
                    #G
                elif i == 72:
                    list2.append("....") 
                    #H
                elif i == 73:
                    list2.append("..") 
                    #I
                elif i == 74:
                    list2.append(".---") 
                    #J
                elif i == 75:
                    list2.append("-.-") 
                    #K
                elif i == 76:
                    list2.append(".-..") 
                    #L
                elif i == 77:
                    list2.append("--") 
                    #M
                elif i == 78:
                    list2.append("-.") 
                    #N
                elif i == 79:
                    list2.append("---") 
                    #O
                elif i == 80:
                    list2.append(".--.") 
                    #P
                elif i == 81:
                    list2.append("--.-") 
                    #Q
                elif i == 82:
                    list2.append(".-.") 
                    #R
                elif i == 83:
                    list2.append("...") 
                    #S
                elif i == 84:
                    list2.append("-") 
                    #T
                elif i == 85:
                    list2.append("..-") 
                    #U
                elif i == 86:
                    list2.append("...-") 
                    #V
                elif i == 87:
                    list2.append(".--") 
                    #W
                elif i == 88:
                    list2.append("-..-")
                     #X
                elif i == 89:
                    list2.append("-.--")
                    #Y
                elif i == 90:
                    list2.append("--..") 
                    #Z
            return list2
        def binary(self):
            return ''.join([bin(i)[2:] for i in self.list])
        def hex(self):
            
            return ''.join([hex(i)[2:] for i in self.list])

    return Encoder


A = problem8()
ainst = A("0")
print(ainst.binary())