# 1
lst = [1,2,3,4,5]
mean = sum(lst)/len(lst)
print(mean)

# 2
lst = [1, -2, 3, -4, 5]
pos = [x for x in lst if x >= 0]
neg = [x for x in lst if x < 0]
print(pos)
print(neg)

# 3
lst = [1, 2, 3, 4, 5]
result = sum(lst[:-2])
print(result)

# 4
lst = [10, 20, 30, 40, 50, 60]
odd_pos = lst[1::2]
print(odd_pos)

#5
lst = [5, 2, 8, 1, 9]
min_val = lst[0]
for x in lst[1:]:
    if x < min_val:
        min_val = x
print(min_val)