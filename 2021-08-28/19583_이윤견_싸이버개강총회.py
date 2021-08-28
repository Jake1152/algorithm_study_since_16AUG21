from sys import stdin
lines = stdin.readlines()
S, E, Q=lines[0].split()
S_set=set()
E_Q_set=set()
for line in lines[1:]:
    t, name = line.split()
    if t<=S: S_set.add(name)
    if E<=t<=Q: E_Q_set.add(name)
        
print(len(S_set and E_Q_set))
