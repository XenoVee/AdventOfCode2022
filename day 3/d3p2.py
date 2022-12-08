file = open('input')
lines = file.read().splitlines()
total = 0
i = 0
group = []
for line in lines:
	group.append(line)
	i += 1
	if i == 3:
		sect = set(group[0]).intersection(group[1])
		sect = sect.intersection(group[2])
		if ord((str(sect))[6]) >= 97:
			total += ord((str(sect))[6]) - 96
		else:
			total += ord((str(sect))[6]) - 38
		group = []
		i = 0
print(total)