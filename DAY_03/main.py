input = input('Enter with space\n').split(' ')

List1 = [int(num) for num in input]
List2 = list(map(int, input))
List3 = input
for i in range(0, len(input)):
    List3[i] = int(input[i])

print(f'{List1}\n{List2}\n{List3}')

# Output
# [1, 2, 3]
# [1, 2, 3]
# [1, 2, 3]