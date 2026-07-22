'''a=int(input("enter a value:"))
b=int(input("enter b value:"))

if a>b:
    print("hello")
'''


'''''
a=int(input("enter a year:"))

if a%400==0 |(a%4==0 & a%100 != 0):
    print("it is a leap year")
else:
    print("it is not leap year")
    '''
    
    
    
    
'''   
def pos_neg(a):
    if a >0:
        print("a is positive")
    else:
        print("a is negitive")
pos_neg(-1)
'''      
 
 
 
 
'''
a=int(input())
if a>0:
    print("positive")
elif a<0:
    print("negitive")
else:
    print("zero")
'''


'''''
a=int(input())
b=int(input())
c=int(input())

if a>b and a>c:
    print("largest number is :",a)
elif b>a and b>c:
    print("largest number is :",b)
else:
    print("largest number is :",c)
'''''



''''
a = int(input("Enter a number: "))

c = 0

while a > 0:
    b = a % 10
    c = c * 10 + b
    a = a // 10

print("Reversed number is:", c)
'''''




'''''
a=int(input())
count=0
while a>0:
    count=count+1
    a=a//10
print("count is :",count)
'''''



'''''   
student_marks=int(input())
if student_marks>85:
    print("student_marks are 90%")
elif student_marks>70:
    print("student_marks are 80%")
else:
    print("student_marks are below 79%")
'''





'''
a=int(input())
b=0
for i in range(0,len(a)):
   a=a//10
   b+=1
print(b)
'''

''''
num=[]
for i in range(4):
    num1=int(input())
    num.append(num1)
num.sort()
print("second largest",num[-2])
'''




'''''
username=input("username")
password=int(input("password"))
if username=="admin" and password==123:
  print("success")
'''''




''''
n=int(input())
for i in range (1,n+1):
   for j in range (1,i+1):
      print("*",end="")

   print()    
'''''


''''
a=int(input())
if a%2==0:
    print("even")
'''   

'''''
a=int(input())
b=int(input())
c=int(input())

print("total=",a+b+c)
print("average=",(a+b+c)/3)
if (a+b+c)/3>=40:
    print("result=pass")
 '''
 
 
 
 
'''''
a=int(input())
if a<=100:
    print(a*5)
elif a>100 and a<100:
    print((100*5) and ((a-100)*7))
else:
    print((100*5)+(100*7)+((a-200)*10))
'''''




''''
a=10000
b=int(input())
if b<=a:
    print("your remaining balance:",a-b)
else:
    print("insufficinet balance")
'''





'''''
a=int(input("enter sub 1:"))
b=int(input("enter sub 2:"))
c=int(input("enter sub 3:"))
d=int(input("enter sub 4:"))

average=(a+b+c+d)/4
print("total:",a+b+c+d)
print(average)

if average >= 90:
    print("grade:A")
elif average >= 75:
    print("grade:B")
elif average >= 60:
    print("grade:C")
elif average >= 40:
    print("grade:C")
else:
    print("Fail")
'''






'''''
a=int(input()) 
count=0
even=0
odd=0
while a >0:
    digit = a % 10
    if a%2==0:
         even+=1
    else:
        odd+=1
    count+=1
    a=a//10
print("total",count)
print("even",even)
print("odd",odd)
'''




'''''
a=25
while True :
    b=int(input())
    if b<a:
       print("retry:too low")
    elif b>a:
       print("retry:too high")
    else:
       print("your guess is correct")
'''''


'''''
quantity=int(input())
price=3000
total=quantity*price
print("product name : laptop")
print("quantity",quantity)
print("price: 3000")
print("total",total)
if total>5000:
     discount=(total*10)/100
else:
    print("no discount")
print("discount",discount)
print("final amount:",total-discount)
'''




'''''
balance=10000
while True:
    print("______main menu_______")
    print("1.check balance")
    print("2.deposite")
    print("3.withdraw")
    print("4.exit")
    choose_one=int(input("enter your checking number:"))
    if choose_one==1:
        print("your balance is:",balance)
    elif choose_one==2:
        deposite=int(input("enter amount"))
        amount=deposite+balance
        print("your balance after deposite:",amount)
    elif choose_one==3:
        withdrawn=int(input())
        if withdrawn<balance:
            balance_amount=balance-withdrawn
            print("your balance after withdraw:",balance_amount)
        else:
            print("insufficient balance")
    elif choose_one==4:
        print("thank you vist again")
        break
    else:
        print("choose only 1 to 4, try again")
'''



       