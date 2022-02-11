import kerthan

while True:
	text = input('Kerthan > ')
	result, error = basic.run(text)

	if error: print(error.as_string)
	else: print(result)