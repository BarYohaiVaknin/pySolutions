nums = [-10,7,19,15]
target = 9
sortNums = nums
sortNums = sorted(sortNums)
findex = 0
lindex = len(nums)-1
s1 = s2 = -1


while findex != lindex:
    if target < sortNums[findex] + sortNums[lindex]:
        lindex -= 1
    elif target > sortNums[findex] + sortNums[lindex]:
        findex += 1
    else:
        s1 = findex
        s2 = lindex
        break

flag = False
for i in range(len(nums)):
    if nums[i] == sortNums[s1] and not flag:
        s1 = i
        flag = True
    elif nums[i] == sortNums[s2]:
        s2 = i
print(s1, s2)












