print("Welcome to the simple calculator program!") #印歡迎語
s = "yes" #設定迴圈執行的規則
while s == "yes":
	a = float(input("Enter the first number:")) #轉成浮點數
	b = float(input("Enter the second number:"))#轉成浮點數
	operation = input("Select an arithmetic operation(＋,-,*,/）:")#選擇計算模式
	if operation == "+" :#設定各計算模式
		print("Result:",a+b)
	elif operation == "-" :
		print("Result:",a-b)
	elif operation == "*" :
		print("Result:",a*b)
	elif operation == "/" :
		if b == 0.0 :#當模式為除法且分母為０
			print("Error: Division by zero!")
		else:
			print("Result:",a/b)
	if operation == "/" and b== 0.0 :
		break
	else:
		s = input("Do you want to perform another calculation?(yes or no):")
if s == "no":#如果執行規則已不成立則輸出Goodbye
	print("Goodbye!")