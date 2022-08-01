lim = int(input("Enter a value:"))
x = 0

print("The limit is " , lim)
while(x < lim):
    x+=1
    if((x % 2) != 0):
        print(x)
    else:
        continue