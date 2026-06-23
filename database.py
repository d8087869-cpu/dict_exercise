# 1
agent = {'name':'alpha', 'level': 3, 'active': True}
print(agent)
#2 
print(agent['name'])
#3 
if agent['level']:
    print(agent.get('level'))
else:
    print(0)
agent['score']=95   
print(agent)
agent['level']=5
print(agent)