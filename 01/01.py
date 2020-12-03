with open('./expense report.txt') as f:
    expenses = f.readlines()
# fjern \n
expenses = [x.strip() for x in expenses]
# konverter til int
expenses = list(map(int, expenses))
#enumerate
for i, j in enumerate(expenses):
    for k in expenses[i:]:
        if j+k == 2020:
            print(j*k)

for i, j in enumerate(expenses):
    for k, l in enumerate(expenses[i:]):
        for m in expenses[k:]:
            if j + l + m == 2020:
                print(j*l*m)