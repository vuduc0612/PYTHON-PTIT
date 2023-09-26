from functools import*
class Cathi:
    def __init__(self, id, date, time, id_class):
        self.id = id
        self.date = date
        self.time = time
        self.id_class = id_class

    def __str__(self):
        return f"{self.id} {self.date} {self.time} {self.id_class}"
def cmp(a, b):
    if a.date != b.date:
        if a.date > b.date: return 1
        else: return -1
    elif a.time != b.time:
        if a.time > b.time:
            return 1
        else:
            return -1
    if a.id > b.id: return 1
    return -1
f = open("D:\IT\Python\Python PTIT\TH\CATHI.in", "r")
a = f.read().split("\n")
n = int(a[0])
ds, idx, i = [], 0, 1
while len(ds) < n:
    id = str(idx + 1)
    while len(id) < 3: id = '0' + id 
    id = "C" + id
    ds.append(Cathi(id, a[i], a[i + 1], a[i + 2]))
    i += 3
    idx += 1
ds.sort(key = cmp_to_key(cmp))
for x in ds:
    print(x)