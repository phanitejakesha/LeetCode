def employeeDays(data,m):
    allYes = ''.join(['Y']*len(data[0]))
    count = 0  
    maxVal = 0
    for i in range(0,len(data)):
	if data[i] == allYes:
		count = count +1
	else:
		if maxVal < count:
			maxVal = count
		count = 0
	if maxVal < count:
                        maxVal = count
    return maxVal
