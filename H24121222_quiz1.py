input_sv = input('Please input a Richter scale value: ')#輸入芮氏規模值（字串）
sv = float(input_sv)#將字串改為浮點數
J = 10**(1.5*sv+4.8)#代入公式計算焦耳值
T = J/(4.184*(10**9))#代入公式計算噸TNT
L = J/2930200 #代入公式計算午餐份數
print("Richter scale value:",sv)#印出芮氏規模值
print("Equivalence in Joules:",J)#印出焦耳值
print("Equivalence in tons of TNT:",T)#印出噸TNT
print("Equivalence in the number of nutritious lunches:",L)#印出午餐份數