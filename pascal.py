import sys

n = int(sys.argv[1])

pasc_list = []
for row in range(n): 
	temp_list = []
	for col in range(row+1):
		if col==row or col==0:
			temp_list.append(1)
		else:
			temp_list.append(pasc_list[row-1][col-1]+pasc_list[row-1][col])
	pasc_list.append(temp_list)
print(pasc_list)




