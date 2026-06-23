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
#10 
list = [1, 2, 3]
set1 = {1, 2, 3}
tuple = (1, 2, 3)
print(list, set1, tuple)
#list allow duplicates , set=you can remove duplicates ,tuple-no changes
#part 2 
a = {1, 2, 3}
b = {3, 4, 5}
print(a.issubset(b))
print(a.issuperset(b))
#2
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
print(pairs[1])
print(pairs[1][1])
#3
number = [1, 2, 2, 3, 3, 3]
diffe = set(number)
print(diffe)
#4
print(a.symmetric_difference(b))
#5
s = {1, 2, 3}
s.add((4, 5))
#list can be change so thir hash also change
#tuple dont change 
#set need fixed iteam