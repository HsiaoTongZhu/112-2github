input_amount = input("Enter the shopping amount:")#輸入金額
input_level = input("Enter the membership level(Regular or Gold):")#輸入會員身份
amount = int(input_amount)#將字串轉為整數
money = 0 #先設定金額為零，透過後面計算出最終金額
if input_level == "Regular":#設立條件
	if amount > 3000:
		money = amount*0.8
	elif amount > 2000:
		money = amount*0.85
	elif amount >1000:
		money = amount*0.9
	else:
		money = amount*1.0
	print(input_level,money)#印出結果
elif input_level == "Gold":
	if amount > 3000:
		money = amount*0.75
	elif amount > 2000:
		money = amount*0.8
	elif amount >1000:
		money = amount*0.85
	else:
		money = amount
	print(input_level,"$",money)
else:
	print("Invalid membership level.Please enter \'Regular\' or \'Gold\'.")
