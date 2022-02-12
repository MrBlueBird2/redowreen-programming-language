import math

while True:
	text = input('Comthon > ')
	if "+" in text:
		ans = 0
		text = text.replace("+", " ")
		text = text.split()
		for i in text:
			if "." in i:
				i = float(i)
				ans += i
			else:
				i = int(i)
				ans += i
		print(ans)
	elif "*" in text:
		ans = 1
		text = text.replace("*", " ")
		text = text.split()
		for i in text:
			if "." in i:
				i = float(i)
				ans *= i
			else:
				i = int(i)
				ans *= i
		print(ans)
	elif '-' in text:
		ans = 0
		text = text.replace("-", " ")
		text = text.split()
		default = int(text[0])
		for i in range(1, len(text)):
			answer = default - int(text[i])
			default = int(text[i])
			ans += answer
		print(ans)