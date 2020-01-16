password = 'a123456'
i= 3
while True:
	ans = input('請輸入密碼？')

	if ans == password:
		print('登入成功！')
		break
	else:
		i = i - 1
		print('密碼錯誤！剩下 ', i ,'機會')
		if i ==0:
			break
