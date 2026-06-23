#1
tags = {'python', 'bash', 'git', 'python'}
print(tags)
print(len(tags))
#2
tags.add('linux')
print(tags)
#3
tags.discard('bash')
print(tags)
tags.discard('c+')
print(tags)
#4 
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
#5
print('git' in tags)
#6 
point = (10, 20)
print(point)
print(point[0], point[1])
#7
#point[0]=99
#tuple cant be change
#8
rgb = (255, 128, 0)
r,g,b =rgb
print(r,g,b)
#9
coords = (1, 2, 3, 2, 1)
print(coords.count(2))
print(coords.index(3))