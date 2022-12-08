def determine_score(input1, input2):
	if input1 == "X": #need to lose
		if input2 == "A": #opponent rock
			return 3 #return scissors
		if input2 == "B": #opponent paper
			return 1 #return rock
		if input2 == "C": #opponent scissors
			return 2 #return paper
	if input1 =="Y": #need to draw
		if input2 == "A": #opponent rock
			return 1 #return rock
		if input2 == "B": #opponent paper
			return 2 #return paper
		if input2 == "C": #opponent scissors
			return 3 #return scissors
	if input1 == "Z": #need to win
		if input2 == "A": #opponent rock
			return 2 #return paper
		if input2 == "B": #opponent paper
			return 3 #return scissors
		if input2 == "C": #opponent scissors
			return 1 #return rock

file = open('input')
lines = file.readlines()
score = 0
for line in lines:
	if line[2] == 'X':
		score += 0
	if line[2] == 'Y':
		score += 3
	if line[2] == 'Z':
		score += 6
	score += determine_score(line[2], line[0])
print(score)
