def quick_merge(l1,l2):
    b = []
    p1 = 0
    p2 = 0
    while p1 < len(l1) and p2 < len(l2):
        if l1[p1] < l2[p2]:
            b.append(l1[p1])
            p1 += 1
        else:
            b.append(l2[p2])
            p2 += 1
    if p1 < len(l1):   
        b += l1[p1:]
    if p2 < len(l2):
        b += l2[p2:]        
    return b  
      
l1 = [int(c) for c in input().split()]
l2 = [int(c) for c in input().split()]
print(quick_merge(l1,l2))    