def find_ins_idx(r, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    
    return len(r)

d = [2,4,5,1,3]
print(find_ins_idx(d, 3))