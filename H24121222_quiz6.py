alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ans = random(0,25)#選出隨機數字

time = 0 #記錄次數
time1 = 0
time2 = 0
time3 = 0
time4 = 0
time5 = 0
time6 = 0
time7 = 0

while alphabet.index(guess) == ans:#當沒猜對，記錄次數並重新猜
	
	if alphabet.index(guess) < 4:
		time1 += 1
		time += 1
	if 3 < alphabet.index(guess) < 8:
		time2 += 1
		time += 1
	if 7 < alphabet.index(guess) < 12:
		time3 += 1
		time += 1
	if 11 < alphabet.index(guess) < 16:
		time4 += 1
		time += 1
	if 15 < alphabet.index(guess) < 20:
		time5 += 1
		time += 1
	if 19 < alphabet.index(guess) < 24:
		time6 += 1
		time += 1
	if 23 < alphabet.index(guess) < 26:
		time7 += 1
		time += 1
	if alphabet.index(guess) < ans:
		print("The alphabet you are looking for is alphabetically lower")
		guess = input("Guess the lowercase alphabet:")
	if alphabet.index(guess) > ans:
		print("The alphabet you are looking for is alphabetically higher")
		guess = input("Guess the lowercase alphabet:")

if alphabet.index(guess) == ans:
		print("Congratulations! You guessedthe alphabet",alphabet.index(guess),"in",time,"tries")





