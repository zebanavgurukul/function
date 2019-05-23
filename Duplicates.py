list_1 = [19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
i = 0
new_1 = []
while i < len(list_1):
	if list_1[i] not in new_1:
		new_1.append (list_1[i])
	i = i + 1
print new_1
