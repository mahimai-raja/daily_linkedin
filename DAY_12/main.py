import textwrap

input = "Hey! iKurious Here ..."

wrapper = textwrap.TextWrapper(width=3)
List = wrapper.wrap(text=input) 

print (List)

''' OUTPUT :
['Hey', '! i', 'Kur', 'iou', 's H', 'ere', '...']
'''