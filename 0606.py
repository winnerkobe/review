data = []
with open ('reviews.txt', 'r') as x:
	for line in x:
		data.append(line)
print(len(data))
print(data[0])