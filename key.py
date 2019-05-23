keys = ["a","b","c","d","e"] 
values = [1,2,3,4,5]
i = 0
new_1 = []
while i < len(keys):
	j = 0
    	while j < len(values):
        	if values[i] not in new_1:
            		new_1.append(values[i])
        	elif keys[i] not in new_1:
            		new_1.append(keys[i])
        	j = j + 1
    	i = i + 1
print new_1
