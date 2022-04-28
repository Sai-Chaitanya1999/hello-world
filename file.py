f = open("new.txt", "r")
g = open("new1.txt", "a")
for x in f:
  g.write(x)
f.close()
g.close()
g = open("new1.txt", "r")
print(g.read())