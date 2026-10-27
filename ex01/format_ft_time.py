import datetime as dt


def format_ft_time():
	a = dt.datetime(1970, 1, 1)

	b = dt.datetime.now()

	res = b - a
	seconds = res.total_seconds() 

	print("Seconds since January 1, 1970:", seconds, "or",  f"{seconds:.6e}", "in scientific notation")
	print(b.strftime("%b"),b.day,b.year)

if __name__ == "__main__":
	format_ft_time()