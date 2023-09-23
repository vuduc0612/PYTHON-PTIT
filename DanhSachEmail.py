f = open("CONTACT.in", "r")
a = f.read().split('\n')
se = set({})
for x in a:
    se.add(x.lower())
for x in sorted(se):
    print(x)
