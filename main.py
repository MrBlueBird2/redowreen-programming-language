import math

while True:
	text = input('Comthon > ')
	l = []
	if "+" in text:
		text = text.replace("+", "plus")
		splitted_text = text.split()
		print(text)