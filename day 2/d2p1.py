def determine_winner(input1, input2):
	if input1 == "A" and input2 == "C":
		return 6
	elif input1 == "C" and input2 == "B":
		return 6
	elif input1 == "B" and input2 == "A":
		return 6
	elif input1 == input2:
		return 3
	else:
		return 0

file = open('input')
lines = file.readlines()
score = 0
for l in lines:
	line = list(l)
	line[2] = chr(ord(line[2]) - 23)
	if line[2] == 'A':
		score += 1
	if line[2] == 'B':
		score += 2
	if line[2] == 'C':
		score += 3
	score += determine_winner(line[2], line[0])
print(score)
