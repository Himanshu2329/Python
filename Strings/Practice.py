# Question 1
# name=input("Enter your name\n")
# print("good after noon "+name)

# question 2
name =input("Enter Your Name\n")
date=input("Enter Date\n")

letter='''Dear <|NAME|>
Your are Selected on
Date <|DATE|>'''

letter=letter.replace("<|NAME|>",name)          
letter=letter.replace("<|DATE|>",date) 
print(letter) 

# Queston 3
print(letter.find(" "))

# Question 4
print(letter.replace(" ","   "))
