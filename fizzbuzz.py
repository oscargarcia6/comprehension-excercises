

for x in range(1,101):
	if x % 3 ==0:
		print(str(x) + " Fizz")
	if x % 5 ==0:
		print(str(x) + " Buzz")
	if x % 3 ==0 and x % 5 == 0:
		print(str(x) + " FizzBuzz")

#for x in range(1,101) if x % 3 ==0 and x % 5 == 0 print(str(x) + " FizzBuzz") if x % 5 ==0 print(str(x) + " Buzz") if x % 3 ==0 print(str(x) + " Fizz")
