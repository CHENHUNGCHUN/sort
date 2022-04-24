a = [645,35,894,6,5465,8745,3284,257434,879485,1]

while True:
    count = 0
    for i in range(len(a)-1):
        b=a.copy()
        if a[i+1] < a[i]:
            a[i] = b[i+1]
            a[i+1] = b[i]
            #print(a)
        else:
            count += 1
    if count == len(a)-1:
        break
print(a)