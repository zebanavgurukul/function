list_1 = [58,24,13,15,63,9,8,81,1,78]
i = 0
new=[]
new1=[]
half = len(list_1)/2
while i < len(list_1):
	if i<half:
        	new.append(list_1[i])
    	else:
        	new1.append(list_1[i])
    	i = i + 1
print new
print new1
