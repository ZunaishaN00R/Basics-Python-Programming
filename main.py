'''''print("Zunaisha ",end="")
print("Noor")
list=['table','chair','fan','erase','pen','pencil']
print(list)
list.insert(3,'zunaisha')
print(list)
list.remove('pencil')
print(list)
print(list+['exams','paper','nobody','rubber'])
print(len(list))
print(len(list+['exams','paper','nobody','rubber']))
print(max(list))
print(max(list+['exams','paper','nobody','rubber']))
print(min(list))
print(min(list+['exams','paper','nobody','rubber']))
#tupules
tupule=(89,90,56,34,12)
print(tupule)
#dictionaries
data={'zunaisha':34,
      'zunaira':56,
      'haseeb':45,
      'muqeet':89,
      'meerab':33}
print(data.keys())
print(data.values())
print(data['zunaisha'])
#ifelse
#loops
x=int(input("Enter number "))
for i in range(0,x):
      print (i)
list1=[[56,78,90],[66,99,33],[67,34,45]]
for item in list1:
      for i in item:
            print(i)
#while loop
y=int(input("Enter the number "))
while(y>=4):
      print("Number is greater then 4 ")
      y=int(input())
      if(y==9):
            break
print("Loop ended")
'''#functions
def fun(num1,num2):
      return (num1*num2)
print(fun(7,8))
def fun(num1, num2):
    return ((num1 + num2)/2)
def fun(num1, num2):
    return (num1 * num2)
print(fun(7, 8))