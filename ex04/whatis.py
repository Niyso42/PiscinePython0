from sys import argv

if len(argv) == 1:
	exit()
try:
	assert len(argv) <= 2, "more than one argument is provided"
	num = argv[1]
	numtrip = num.lstrip("-")
	assert numtrip.isdigit(), "argument is not an integer"
	if (int(numtrip) % 2 == 0):
		print("I'm Even")
	else:
		print("I'm Odd")
except AssertionError as e:
	print("AssertionError:", e)
