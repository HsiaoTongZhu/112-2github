
n = int(input("Enter the size of the grid:"))
i = n
while i > 0:#印出題目所要
	print("_ "*n)
	i -= 1
a,b= input("Enter the cell coordinatesto edit:")
value = input("Enter the new value for the cell:")
s1 = ["_ "]*n
s=[s1*n]
i = 0
j = 0
while i < n-1:#原模樣
	while j < n:
		s[i][j] = "_ "
		j += 1
	i += 1
s[a][b] = value#取代成新字
