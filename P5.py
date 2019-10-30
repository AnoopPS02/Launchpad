*program that asks the user for a phrase/sentence & Print back to the user the same string, except with the words in backwards order*

String="My name is Anoop"
String1=String.split()
String2=String1[::-1]
Ans=""
for i in String2:
	Ans=Ans+" "+i
print(Ans)
