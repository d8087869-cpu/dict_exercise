'''
# 1
agent = {'name':'alpha', 'level': 3, 'active': True}
print(agent)
#2 
print(agent['name'])
#3
print(agent.get('level'))
print(agent.get(0))

#4   
agent['score']=95   
print(agent)
agent['level']=5
print(agent)
#6
del agent['active']
print(agent)
#7
print(agent.keys())
print(agent.values())
print(agent.items())
#8
if 'score' in agent:
    print(True)
else:
    print(False) 

#9 
scores={'Alpha': 80, 'Bravo': 95, 'Charlie': 70}
high_score = max(scores, key=scores.get)
print(high_score)

#10 
new_agent = agent.copy()
new_agent['level']=770
print(new_agent)
'''
#part2 
config = {}
config =config.setdefault('timeout',30)
print(config)