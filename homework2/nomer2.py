spicok = []
a = input(" ")
while a:
    spicok.append(a)
    a = input()
spicok.sort(reverse=True)
print("".join(spicok))
