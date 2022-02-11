import math

while True:
	text = input('Comthon > ')
	l = []
	if "+" in text:
		text = text.replace("+", " ")
		text = text.split()
		print(text)