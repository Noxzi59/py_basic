#
##
###
####
#####

"""n=int(input("enter no of rows"))
i=1
while n > 0:
    print("#" * i)
    n=n-1
    i=i+1"""


# upper lower special
"""text=input("enter the text")
upper=lower=special=num=0
for i in  text:
    if i.isupper():
        upper=upper+1
    elif i.islower():
        lower= lower+1
    elif i.isdigit():
        num=num+1
    else:
        special=special+1
print("total no of upper case are = ",upper ,"total numbers of lower case are = ",lower ,"total number of digits are =",num ,"total number of special charecters are= ", special)

"""

#find a sub sting in a string

"""
str1="Artificial Intelligence (AI) is the science and engineering of creating intelligent machines and computer programs capable of performing tasks that typically require human intelligence. These tasks include data analysis, language"
str2=input("enter the thing u wanna count  if not press enter :")
s1=str1.split()
cnt=0
for i in s1:
    if i == str2:
        cnt=cnt+1
print(cnt)

"""



#basic calculator 

"""a= int(input("enter the no 1: "))
b= int(input("enter no 2: "))
print ( " enter + to add")
print ( " enter - to substract")
print ( " enter * to multiply")
print ( " enter / to divide")
print ( " enter . to exit")

ans = 0
def add():
    ans=a+b
    print(ans)

def sub():
    ans = a-b
    print(ans)

def product():
    ans = a * b 
    print(ans)

def divide():
    ans = a//b 
    print(ans)

while True:
    choice= input (" enter your choice") # + 
    if choice == "+":
        #print( a+ b) optionone
        add()
    elif choice == "-":
        sub()
    elif choice == "*":
        product()
    elif choice == "/":
        divide()
    elif choice == ".":
        break
    else:
        print("enter the correct choice")
"""
# 1=3 2=3 1=2 3+2 1+2 
"""no1=10
no2=11
no3=14
sum1= no1 + no2 + no3
sum2= 0
if no1 == no2 :
    sum2=no1+no3
elif no2 == no3:
    sum2 = no2 + no1
elif  no3 == no1:
    sum2 = no2 + no1
else:
    print(sum1)
"""

#(xyz)/xy+yz+zx   3ppl working n hrs find the time when work done
"""x=10
y=15
z=12
print("work will complete in :", (x*y*z)/(x*y+y*z+z*x))"""

#swap

"""x=1
y=2
c=0

c=x #gave the val of x to c
x=y #gave the val of y to x as x contains no val now
y=c #gave the val of c  to y that c took from x.

print(x,y)"""

# avg of n number            
        
"""n=[1,2,3,4,5,6,7,8,9,10]
sumn=0
for i in range(len(n)):
    sumn= sumn +n[i]
print("avg of n numbers is :",(sumn)/(len(n)))
    """
#hight cm in inch ft in inch
"""inp = int(input("Enter your height in cm: "))
inch = inp / 2.54
ft = inch / 12
print("Your height in inches is:", inch)
print("Your height in feet is:", ft)"""


#OBTAIN  From user:: Principle amt || Rate of intrest || time
# claculate Simple Intrest

"""a=0
p=int(input("enter the principal amount"))
r=int(input("enter intrest rate"))
t=int(input("enter time"))
a=(p*r*t)/100
print("Simple intrest of your amt is",a)
"""


# take sec form user
# convert it into min and hrs
"""import math
sec=int(input("enter seconds"))
min= sec / 60
se =  sec % 60
#print(sec,"seconds have ", math.floor(min),"min and ",se, )
print(math.floor(min),".",se,"minuets")
"""

#area of triangel 
"""import math
a=int(input("enter the side"))
area=(math.sqrt(3)/4)*a**2
print(area)"""

#Pythagorus theorum
"""import math
p=int(input("enter a perpendicular"))
h=int(input("enter hypotenious"))
base = math.sqrt((h**2)-(p**2))
print(base)"""

#create a 6 digit otp
"""import random

def generate_otp():
    return random.randint(100000, 999999)

otp = generate_otp()
print("Your OTP is: ",otp)
"""

#radious of sphear
"""
PI=3.14
r=int(input("enter the radious"))
print("area of sphear is",(4*PI)*r**2)
"""

#volume of cylender
"""
PI=3.14
r=int(input("enter the radious"))
h=int(input("enter the hight"))
"""