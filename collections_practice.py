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