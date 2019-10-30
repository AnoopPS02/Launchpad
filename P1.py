from datetime import *
present = str(date.today())
now = present.split()[0].split("-")[0]
Name=input("Enter your name : ")
Age=int(input("Enter your Age : "))
print("Hey ! "+Name.split(" ")[0]+" you'll turn 100 years in "+str(int(now)+100-Age))
