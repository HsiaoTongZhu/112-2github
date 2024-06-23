sequence = input("Enter a sequence of integers seperated by whitespaces:")#輸入字串
s = sequence.split(" ")#把字串用空格隔開
s.sort()#排序
i = 1
while i < len(s):
	if s[i]==s[i-1]:#若兩者相等
		s.remove(s[i-1])#
	i += 1
n = int(input("Length:"))
print("LICS:",s[:n])