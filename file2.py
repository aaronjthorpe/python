# for i in [1,2,3,4,5]:
	# print(f"The square of {i} is {i ** 2}")

def square_number(num: int) -> float:
	return float(num ** 2)

while True:
	user_input = input("Enter a number to square or 'x' to exit: ")
	if user_input in ('x','X'):
	# if user_input == 'x' or user_input == 'X':
		break
	else:
		try:
			print(square_number(int(user_input)))
		except ValueError as e:
			print(f"Could not convert {user_input} to integer.")
			print(f"Error text: {e}")