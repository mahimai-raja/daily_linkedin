numbers = input('Enter numbers with space :\n').split()
numbers = [int(i) for i in  numbers]
numbers = list(set(numbers))
seqNum = int(input('Enter fair number \n'))

posi = []
nega = []
answer = []

for num in numbers:
    if num >= 0 :
        posi.append(num)
    elif num < 0 :
        nega.append(num)

for i in range(seqNum):
    try:
        answer.append(posi[i])
    except:
        pass
    try:
        answer.append(nega[i])
    except:
        pass

answer = answer[:seqNum]

print(answer)
