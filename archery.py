import fileinput

def isInsideOfCircle(R, x, y):
	return (x ** 2 + y ** 2) <= (R ** 2)

def countQs(R_list, point_pair_list):
	counter = 0
	for line in point_pair_list:
		for r in R_list:
			firstIn = isInsideOfCircle(r, line[0], line[1])
			secondIn = isInsideOfCircle(r, line[2], line[3])
			if (firstIn and not secondIn) or (not firstIn and secondIn):
				counter +=1
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