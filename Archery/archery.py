import fileinput

def isInsideOfCircle(R, x, y):
	return (x ** 2 + y ** 2) <= (R ** 2)

def getMinRadius(R_list, x, y):
	"""binary search routine to find minimum circle with radius R which contains point """
	lo = 0
	hi = len(R_list)-1
	while lo <= hi:
		mid = lo + (hi-lo)/2
		tryR = isInsideOfCircle(R_list[mid], x, y)
		if tryR:
			hi = mid - 1
		else:
			lo = mid + 1
	return hi



def countQs(R_list, point_pair_list):
	counter = 0
	for line in point_pair_list:
		#find minimum radius of circle which contains first point
		first_r_min = getMinRadius(R_list, line[0], line[1])
		#find minimum radius of circle which contains second pont		
		second_r_min = getMinRadius(R_list, line[2], line[3])
		#print "for line %s first min = %s second min = %s" % (line, first_r_min, second_r_min)
		counter += abs(first_r_min - second_r_min)
	return counter

def main():
	input = fileinput.input()
	i = 0
	n = int(input[0])
	R_list = [int(elem) for elem in input[1].rstrip("\n").split(" ")]
	R_list.sort()
	m = int(input[2])
	point_pair_list = []
	for j in range (0,m):
		(x1, y1, x2, y2) = tuple([ int (elem) for elem in input[3+j].rstrip("\n").split(" ")])
		point_pair_list.append((x1, y1, x2, y2))
	print countQs(R_list, point_pair_list)

if __name__ == '__main__':
	main()