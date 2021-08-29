lst = [6,5,7,1,2,6,9,8]
count = 0
while count < len(lst):     #控制循环次数
    i = 0
    while i < len(lst) - 1:
        if lst[i] > lst[i+1]:
            lst[i],lst[i+1] = lst[i+1],lst[i]
        i = i + 1
    count = count + 1
print(lst)