#cerintele 2, 14

def readList():
	n = int(input("Numarul de elemente din lista: "))
	lis = []
	print("Elementele listei (cate unul pe linie):")
	for i in range(n):
		lis.append(int(input()))
	return lis
