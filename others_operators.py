#1)Identity operator
#it only return true or false
#it only works on small value

#There are two identity operator=> is and is not
num1=10
num2=10
print(num1 is num2)  #result:True
print(num1 is not num2)  #result:False

str1="lily"
str2="sunflower"
print(str1 is str2) #result:False
print(str1 is not str2) #result: True

#identity operators does not work on large dataset
list1=[10,20,30]
list2=[10,20,30]
print(list1 is list2) #result:False


#2) Membership Operator
#There are two membership operators:=> in and not in
users=["varun","Amit", "Sourav","Debashis"]
if("Triparna" in users):
    print("Acess granted...... ")
else:
    print("Acess denied")
if("Sourav" not in users):
     print("Acess denied...... ")
else:
    print("Acess granted")
name=input("Enter your name")
if (name in users):
     print("Acess granted...... ")
else:
    print("Acess denied")