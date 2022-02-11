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