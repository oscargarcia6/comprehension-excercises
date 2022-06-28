

list2= [ "fizzBuzz" if (x % 3 ==0 and x % 5 == 0) else "fizz" if (x % 3 ==0) else "buzz" if (x % 5 ==0) else x for x in range(1,101)]


print (list2)

for x in range(1,101):
	if x % 3 ==0:
		print(str(x) + " Fizz")
	if x % 5 ==0:
		print(str(x) + " Buzz")
	if x % 3 ==0 and x % 5 == 0:
		print(str(x) + " FizzBuzz")