# Python practise



# For Loops


# 1]
# size=int(input());
# list=[ int(i) for i in  input().split()];

# for i in list:
#     print(i,end=",");





# 2]
# list=[];

# for k in range(3):
#     i=int(input());
#     list.append(i);
   

# for i in list:
#     print(i,end=" ");




# while Loop
# j=1
# while(j<10):
#     print(j);
#     j=j+1;



# list=[45,90,120,89,78];
# list=list[2:4:2]
# for i in list:
#     print(i,end=" ");
    
# print()
# del list[index]
# list.remove(45);

# for i in list:
#     print(i,end=" ");



# substring of a given string

# st="My name is kousik roy";
# st=st[2:8:1];
# for i in st:
#     print(i,end="");









# function
# def sum(n1,n2):
#     return n1+n2;

# n1=int(input());
# n2=int(input());
# print("The Sum of the no is : ",end="")
# print(sum(n1,n2));

# def prime(n):
#     for d in range(2,n):
#         if (n%d==0):
#             print(d);

#     return True;

# n=int(input());

# prime(n);







# Tuplse  - >  assingning different values to same variables create tuple in python by default
# tuples are immutable
# b=4,5,6,10,16,90
# print(b);
# print(type(b));
# # accesing tuple is the same way as we do in arrays 
# print(b[0]);
# # slicing in tuples
# print(b[0:4]);


# # list to tuples
# lst=[12,23,4,5,6,9];
# c=tuple(lst);

# print(c);
# print(min(c));



# giving more arguments to a function
# def sum(a,b,*more):
#     ans=a+b;
#     for i in more:
#         ans=ans+i;
    
#     return ans;

# n=sum(34,2,3,4,2);
# print(n);







# Dictionary

# a={33:"jei",45:32,24:323,42,4,3,2,5,6};
# b=dict([("one",1),("two",2)])
# print(b["one"])






# set

# a={3,4,5,2,6,7,343,44,23,56,78}
# print(type(a))
# a.add(8);
# print(a);
# a.add(8);
# print(a);


# intersections
# a={2,3,4};
# b={4,5,6};
# print(a.intersection(b))


# Union

# tuple1={1,2,3,4};
# tuple2={5,6,7,8};
# print(tuple1.union(tuple2));


# code to calculate the expenses of hostel 

# Amt_per_month=7500

# def one_year_plan(month):
#     return month*Amt_per_month;

# months=int(input());
# total_amount = one_year_plan(months);
# print("The total cost to sustain in this hostel will be : ",total_amount)











# object and clases in py
# object has two types of attributes instance and class
# internally the object creates an dict for the class

# class Student:
#     pass;

# S1=Student();
# S1.name="Kousik Roy"
# S1.roll_no="20EC074"
# S1.Age=18;

# S2=Student();


# print(S1.__dict__);

# # inbuilt function for an attribute
# print(hasattr(S1,"name")); #return an boolean value
# print(getattr(S1,"name","Aman")); #return an boolean value (obj,attr,default value)
# print(setattr(S1,"Father name","Jaishankar Roy")); 
# print(delattr(S1,"name"));

# # class attribute can be defined by 
# Student.teacherName="Pushpa";
# print(Student.__dict__)
# print(S1.teacherName)



# by default the function which we define in class is of object and it passes obj as argument we use self as this in py
# self point to that object 

# class Student :
#     def printHelllo(self):
#         name="aman roy"
#         print("Hello " + self.name);
#         print("Hello " + name);


# S1=Student();
# S1.name="Kousik roy";
# S1.printHelllo();

# s2=Student();
# s2.printHelllo();








# constructor in py

# class Student:
#     def __init__(self):
#         pass







# acess modifier in py

# public : by default;
# private : __ after varable or function;
# protected : _ after varable or function;