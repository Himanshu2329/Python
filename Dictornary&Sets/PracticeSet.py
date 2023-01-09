# # Question 1
# my={"Pankha":"fan","loha":"metal","kursi":"chair"}
# print("search ",my.keys())
# a=input("enter the hindi word\n")
# # print("translation "+my[a])
# print("translation ",my.get(a))

# # question 2
# num1=int(input("enter number: "))
# num2=int(input("enter number: "))
# num3=int(input("enter number: "))
# num4=int(input("enter number: "))

# b={num1,num2,num3,num4}
# print(b)

# # Question 3
# he={12,"12"}
# print(he)

# Question 4

favlang={}
a=input("Enter your fav lang shubham\n")
b=input("Enter your fav lang ankit\n")
c=input("Enter your fav lang anna\n")
d=input("Enter your fav lang mike\n")

favlang["shubham"]=a
favlang["ankit"]=b
favlang["anna"]=c
favlang["ankit"]=d
print(favlang.get("ankit"))
