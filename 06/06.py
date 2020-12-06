
with open('./customs declaration.txt') as f:
    customs_declaration = f.read()

customs_declaration = customs_declaration.split('\n\n')

# part 1
customs_declaration_1 = [set(x.replace('\n', '')) for x in customs_declaration]
print(sum(map(len, customs_declaration_1)))

# part 2
customs_declaration_2 = [(x.split('\n')) for x in customs_declaration]
customs_declaration_2 = [[set(x) for x in y] for y in customs_declaration_2]
customs_declaration_2 = [set.intersection(*x) for x in customs_declaration_2]
print(sum(map(len, customs_declaration_2)))