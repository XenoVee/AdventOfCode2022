file = open('input')
lines = file.readlines()
current = 0
highest = 0

for line in lines:
	if line != '\n':
		current += int(line)
	if line == '\n':
		if current > highest:
			highest = current
		current = 0
print("highest: " + str(highest))
file.close