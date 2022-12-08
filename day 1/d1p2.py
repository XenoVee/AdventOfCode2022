file = open('input')
lines = file.readlines()
current = 0
first = 0
second = 0
third = 0

for line in lines:
	if line != '\n':
		current += int(line)
	if line == '\n':
		if current >= first:
			third = second
			second = first
			first = current
		elif current >= second:
			third = second
			second = current
		elif current >= third:
			third = current
		current = 0
print("first: " + str(first) + " + " + str(second) + " + " + str(third) + " = " + str(first + second + third))
total = first + second + third
print(total)
file.close