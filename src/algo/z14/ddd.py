from datetime import datetime

st = datetime.now().timestamp()
s = 0
while s < 10**9:
    s += 1

ed = datetime.now().timestamp()
print(f'lasted: {ed-st:.3f}s')
