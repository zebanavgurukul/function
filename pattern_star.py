n = 4
i = 1
while i < n:
	if (i == n - 1 and i > 0):
	        n = n - 1
	        print ("$" *i)
	        i = i - 1
	        continue
	elif i == 0:
	        break
	print (i* "$")
	i = i + 1
