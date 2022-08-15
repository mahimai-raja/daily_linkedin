# Author : Mahimai Raja J
# Linkedin : https://www.linkedin.com/in/mahimai-raja-j/

List1 = [1,3,4]
List2 = [2,3,4,5]
List3 = [2,3,4,6]

unCommon = set(List1) ^ set(List2) ^ set(List3)
print(unCommon)


