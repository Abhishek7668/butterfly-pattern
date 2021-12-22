raw = 20

for i in range(1,raw+1):
    for j in range(1,i+1):
        print("*",end="")
    for l in range(1,raw-i+1):
        print("",end=" ")
    for k in range(1,raw-i+1):
        print("",end=" ")
    for p in range(1,i+1):
        print("*",end="")

    print()
for i in range(raw,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    for l in range(1,raw-i+1):
      print("",end=" ")
    for k in range(1,raw-i+1):
        print("",end=" ")
    for p in range(1,i+1):
       print("*",end="")
    print()
