a = [
    ['Xizhi', 50000, 'Hangzhou'],
    ['Yizhou', 40000, 'Singapore'],
    ['Juzhen', 30000, 'Huaihua'],
    ['Houxuan', 20000, 'Guiyang'],
]

for i in range(len(a)):
    for j in range(len(a[1])):
        print(a[i][j], end="\t")
    print()
