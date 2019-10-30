List=[1, 2, 3, 2, 0, 65, 21, 4, 2, 10]
Ans=[]
Key = 2
for i,j in enumerate(List):
	if j == Key:
		Ans.append(i)
print(Ans)
