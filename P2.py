*program that prints out all the elements of the list that are less than 5*

List=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Ans=[]
for i in (List):
	if i<5:
		Ans.append(i)
print(Ans)
