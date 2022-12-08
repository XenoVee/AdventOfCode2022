file = open('input')
lines = file.read().splitlines()
total = 0
for line in lines:
	split1 = set(line[0:len(line)/2])
	split2 = set(line[len(line)/2:len(line)])
	sect = split1.intersection(split2)
	if ord((str(sect))[6]) >= 97:
		total += ord((str(sect))[6]) - 96
	else:
		total += ord((str(sect))[6]) - 38
print(total)