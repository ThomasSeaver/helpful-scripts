filename = str(input("Filename to sort: "))
output = str(input("output name: "))

fin = open(filename, 'r')
fout = open(output, 'w')

total = []

for line in fin:
    line = line[1:len(line)-2]
    line = line.replace(',', '')
    line = line.split(' ')
    total.append([line[0],line[1:]])
fin.close()

total.sort()

for val in total:
    fout.write("(" + val[0] + ", " + val[1][0] + ", " + val[1][1] + ", " + val[1][2] + ")\n")

fout.close()
