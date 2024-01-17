#4일차 과제

#1
e2f = {'dog' : 'chien', 'cat' : 'chat', 'walrus': 'morse'}
print(e2f)

#2
print(e2f['walrus'])

#3
f2e = dict(e2f.items())
print(f2e)

#4
print({k : v for v, k in e2f.items()}['chien'])

#5
print(e2f.keys())

#6
life = {'animals': {'cats':'Henri', 'octopi' : 'Grumy', 'emus' : 'Lucy'} , 'plants' : {}, 'other' : {}}

#7
print(life.keys())

#8
print(life['animals'].keys())

#9
print(life['animals']['cats'])

#10
squares = {i : i**2 for i in range(10)}
print(squares)
















