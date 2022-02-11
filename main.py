import kython

while True:
	text = input('Kython > ')
	result, error = kython.run(text)

	if error: print(error.as_string( ))
	else: print(result)