squares = []
for x in range(10):
	squares.append(x**2)

squares	

# same as above
squares = list(map(lambda x: x**2, range(10)))

# same as above
squares = [ x**2 for x in range(10)]

# same as above 1
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# same as above 1
[(x, y) for x in [2,5,6,3] for y in [4,3,6,5] if x !=y ]
# same as above 1
 combs = []
for x in [1, 2, 3]:
	for y in [3, 1, 4]:
		if x != y:
			combs.append((x, y))

combs

vec = [ -4, -2, 0, 2, 4]
[x*2 for x in vec]

[x for x in vec if x >= 0]

[abs(x) for x in vec]
# abs = absolute value in integer or float

freshfruit = [' banana','loganberry','passion fruit ']
[weapon.strip() for weapon in freshfruit ]

[(x, x**2) for x in range(6)]

vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

num = [[1, 2, 3, 4, 5], [5, 6, 7, 8, 1,9], [4, 9, 3, 6, 8, 3]]

num[0][3]
num[2][2]
num[1][4]
num[2][4]
num[0][0]
num[]

# matix funtion start from here
matrix = [
	[1, 2, 3, 4]
	[5, 6, 7, 8]
	[9, 10, 11, 12],
]

[[row[i] for row on martix] for i in range(4)]


for i in range (4):
	for row on martix:
		row[i]


transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed

transposed = []
for i in range(4):
	transposed_row = []
	for row in martix: 
		transposed_row.append(row[i])
	transposed.append(transposed_row)

transposed

