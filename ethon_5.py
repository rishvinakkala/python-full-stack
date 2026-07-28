# for i in range(1,21,2):
#     print(i)




# x=int(input("enter number: "))
# if x < 0:
#     print(x," is negitive")
# elif x > 0:
#     print(x," is positive")
# else:
#     print("zero")






# num=1234
# total=0
# while num > 0:
#     total += num % 10
#     num //= 10
# print(total)








# n=int(input())
# for i in range(1,11):
#     print(f'{n} x {i}={n*i}')





















# x=int(input("enter number: "))
# if x < 0:
#     print(x," is negitive")
# elif x > 0:
#     print(x," is positive")
# else:
#     print("zero")



# students = [
#     {"name": "ravi", "marks": 89},
#     {"name": "rakesh", "marks": 78},
#     {"name": "tulasi", "marks": 78}
# ]

# for student in students:
#     print(student["name"], ":", student["marks"])




# n = "the end of the year"
# vowels = 'aeiouAEIOU'
# count = sum(1 for ch in n if ch in vowels)
# print('Vowel count:', count)







# class student:
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course

#     def display(self):
#         print(f"name:{self.name},age{self.age}")
#     def study(self):
#         print(f"{self.name} is studying {self.course}")
# s=student("krishna",22,"mca")
# s.display()
# s.study()




      
# class circle:
#     pi=3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return circle.pi *self.radius ** 2
# c=circle(5)
# print(c.area())
        
        
        
# class triange:
#     def __init__(self,b,h):
#        self.b=b
#        self.h=h
       
#     def area(self):
#         return  0.5*self.h*self.b
# t=triange(3,6)
# print(t.area())
        
        
        
        

# class person():
#     def speak(slef):
#         print("can speak")
#     def walk(self):
#         print("can walk")  
# class student(person):
#     def study(self):
#         print("can study")
        
# s=student()
# s.speak()
# s.walk()
# s.study()






# class person():
#     def __init__(self):
#         print("person constructor")
# class student(person):
#     def __init__(self):
#         super().__init__()
#         print("student constructor")

# s=student()





class person():
    def __init__(self,name):
        
        self.name=name
    def display_name(self):
        print("name",self.name)
        
class student(person):
    def __init__(self,name, roll_num):
        super().__init__(name)
        self.roll_num=roll_num
    def display_roll_num(self):
        print("roll number",self.roll_num)


s=student("ravi",101)

s.display_name()
s.display_roll_num()
        
        
        
    