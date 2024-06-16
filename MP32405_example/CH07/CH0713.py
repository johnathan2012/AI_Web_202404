from collections import defaultdict

pern = [('Mary', 'F'), ('Tomas', 'M'), ('Grace', 'F'),
         ('Emily', 'F'), ('Eric', 'M')]

#以list為default_factory
dt = defaultdict(list)

# 讀取List -- Tuple元素為key, value
for k, v in pern:
    dt[v].append(k)

dt2 = (list(dt.items()))
print('以性別分組')
print(dt2)
