import fileinput



def main():
	input = fileinput.input()
	i = 0
	n = int(input[0])
	R_list = input[1].rstrip("\n").split(" ")
	m = int(input[2])
	point_pair_list = []
	for j in range (0,m):
		(x1, y1, x2, y2) = tuple(input[3+j].rstrip("\n").split(" "))
		point_pair_list.append((x1, y1, x2, y2))
	print n
	print R_list
	print m
	print point_pair_list



if __name__ == '__main__':
	main()