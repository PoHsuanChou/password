import random
r = random.randint(1, 100)
while True:
	number = input('請輸入數字？')
	number = int(number)
	if number == r:
		print('猜對了！')
		break
	elif number >r :
		
		print('比答案大')
	elif number<r:
		
		print('比答案小')
