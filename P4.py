List=[1,2,2,4,5,6,6,7,7,8]
Ans=[]
for i in List:
	if i not in Ans:
		Ans.append(i)
print(Ans)
