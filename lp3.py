arr=[2, 5, 13 ,7, 76, 3, -1, 0, -54] 
loop_count=0
swap_count=0
for j in range(0, len(arr), 1):
    for i in range(0, len(arr)-j-1, 1):
        if arr[i]>arr[i+1]:
            el=arr.pop(i)
            el2=arr.pop(i)
            arr.insert(i, el)
            arr.insert(i, el2)
            swap_count+=1
        loop_count+=1
        print(arr)
print(loop_count, swap_count)
  

