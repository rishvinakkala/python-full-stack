'''
a = [1,10,30,9,60,20,25]
b = list(filter(lambda x: x%2==0,a)) #even
c = list(filter(lambda y: y%2!=0,a)) #odd
d = list(map(lambda x: x**2,a))
print(b)
print(c)
print(d)
'''



''''
def fact(n):
    if n==0 or n==1:
        return 1
    return n *fact(n-1)
print(fact(8))
'''


''''
s={1,2,3,4,4,56,}
s.add(5)
s.remove(4)
s.discard(2)
print(s)
'''



''''
a={1,2,3,4}
b={3,4,5,6}
print( a | b)
print( a & b)
print(a - b)
print(b - a)
print(a ^ b)
'''




# d={
#     "name":"rishvi",
#     "course":"mca",
#     "year":2,
#     "marks":(12,34,56,78)
# }
''''
print(d["name"])
print(d["year"])
print(d.get("year",0))

del d["name"]
d.pop("marks")
print(d)'''

''''
for key in d:
    print(key,":",d[key])
'''

# print(d.values())
# print(d.items())


''''
s="hello world"
print(s.title())
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.replace("hello","python"))
print(s.find("hello"))
print(s.count("l"))
print(s.startswith("ll"))
print(s.endswith("ld"))
print(len(s))
'''




'''''
file=open("notes.txt","w")
file.write("hello\n")
file.write("world")
file.close()

file = open("notes.txt",'r')
content = file.read()
print(content)
file.close()
'''





'''''
def validate_phone(phone):
    if len(phone) != 10:
        raise ValueError(f"phone number must have 10 digits ")
    return True
try:
    validate_phone("123456")
except ValueError as e:
    print("error",e)
'''''







'''''
while True:
    
    print("--------calculator--------")
    print("1.Addition")
    print("2.subraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")

    a=float(int(input()))
    b=float(int(input()))

    choose=int(input())
    if choose==5:
        print("thank you")
        break
    elif choose==1:
        print(a+b)
    elif choose==2:
        print(a-b)
    elif choose==3:
        print(a*b)
    elif choose==4:
        print(a/b)
    else:
        print("invalid choice")
        '''
        
        
        
        
        
        