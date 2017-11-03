from logger import Logger


def add_numbers(x,y):
	return x + y

if __name__ == '__main__':
	Logger.log_info("-----Starting up the program-----")

	Logger.log_info("Calling divide_numbers")

	new_number = add_numbers(5, 2)
	test_number = 5 + 2
	
	if new_number != test_number:
		Logger.log_error("Numbers did not match up! Faulty implementation")
	else:
		Logger.log_info("Numbers added up correctly!")

