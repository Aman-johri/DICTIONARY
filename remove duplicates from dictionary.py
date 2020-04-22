#remove duplicates from dictionary
d={}
d1={1:"aman",1:"aman",2:"johri"}
for i,j in d1.items():
    if j not in d.values():
        d[i]=j
print(d)
