# i want to print 2 to 10 tables

for i in range(1,11):
    for j in range(2,11):
        print(f"{j}*{i}={i*j}",end="    ")
    print("\n")